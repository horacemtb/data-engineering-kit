import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, expr, split, avg
import pyspark.sql.functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("BostonCrimeAggregation").getOrCreate()

parser = argparse.ArgumentParser(description='Process Boston Crime data')
parser.add_argument('--crime_data', type=str, required=True, help='Path to crime data CSV file')
parser.add_argument('--offense_codes', type=str, required=True, help='Path to offense codes CSV file')
parser.add_argument('--output_path', type=str, required=True, help='Path to output Parquet file')
args = parser.parse_args()

crime_df = spark.read.csv(args.crime_data, header=True, inferSchema=True)
offense_codes_df = spark.read.csv(args.offense_codes, header=True, inferSchema=True)

# Data Cleaning
# Removing duplicates
crime_df = crime_df.dropDuplicates()
offense_codes_df = offense_codes_df.dropDuplicates(['CODE'])

# Removing null values in DISTRICT column
crime_df = crime_df.dropna(subset = ["DISTRICT"])

# Extracting the `crime_type` by splitting the NAME column in offense_codes_df and joining offense_codes_df with crime_df
offense_codes_df = offense_codes_df.withColumn('crime_type', split(col('NAME'), ' - ').getItem(0))
crime_df = crime_df.join(offense_codes_df, crime_df['OFFENSE_CODE'] == offense_codes_df['CODE'], 'left')

# Group by DISTRICT to get the number of total crimes
total_crimes_df = crime_df.groupBy("DISTRICT").agg(F.count("*").alias("crimes_total"))

# Group by district, year, and month to count crimes per month, then calculate the median monthly crimes for each district
monthly_crimes_df = crime_df.groupBy("DISTRICT", "YEAR", "MONTH").agg(count("*").alias("crimes_per_month"))
district_monthly_median = monthly_crimes_df.groupBy("DISTRICT").agg(
    F.expr("percentile_approx(crimes_per_month, 0.5)").alias("crimes_monthly")
)

# Count crime types for each district, then rank crime types by count for each district, select top 3 crime types 
crime_type_counts_df = crime_df.groupBy("DISTRICT", "crime_type").agg(F.count("*").alias("crime_count"))
window_spec = Window.partitionBy("DISTRICT").orderBy(F.desc("crime_count"))
ranked_crime_types_df = crime_type_counts_df.withColumn("rank", F.row_number().over(window_spec))
top_3_crimes_df = ranked_crime_types_df.filter(F.col("rank") <= 3)

# Aggregate crime types into a single string per district, separated with a comma and a space
frequent_crime_types_list_df = top_3_crimes_df.groupBy("DISTRICT").agg(
    F.concat_ws(", ", F.collect_list("crime_type")).alias("frequent_crime_types")
)

# Calculate lat and lng as the average of latitudes and longitudes of incidents in each district
district_coords_df = crime_df.groupBy("DISTRICT").agg(
    F.avg("Lat").alias("lat"),
    F.avg("Long").alias("lng")
)

# Join all dfs (total_crimes_df, district_monthly_median, frequent_crime_types_list_df, district_coords_df)

agg_df = total_crimes_df \
    .join(district_monthly_median, on="DISTRICT", how="left") \
    .join(frequent_crime_types_list_df, on="DISTRICT", how="left") \
    .join(district_coords_df, on="DISTRICT", how="left")

# Write the output to Parquet format
agg_df.write.parquet(args.output_path)

# Stop the Spark session
spark.stop()