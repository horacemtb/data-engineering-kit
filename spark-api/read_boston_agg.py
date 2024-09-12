import argparse
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadBostonAgg").getOrCreate()

parser = argparse.ArgumentParser(description='Read Boston agg data')
parser.add_argument('--agg_data', type=str, required=True, help='Path to agg parquet file')
args = parser.parse_args()

agg_df = spark.read.parquet(args.agg_data, header=True, inferSchema=True)

agg_df.show(12)

spark.stop()