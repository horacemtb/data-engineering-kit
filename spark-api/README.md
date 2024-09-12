1. Connect to VM and run the following commands to install Apache Spark on your Ubuntu machine:

```
sudo apt update
sudo apt upgrade -y
```

```
sudo apt install default-jdk -y
```

```
wget https://dlcdn.apache.org/spark/spark-3.5.2/spark-3.5.2-bin-hadoop3.tgz
```

```
tar xzvf spark-3.5.2-bin-hadoop3.tgz
```

```
sudo mv spark-3.5.2-bin-hadoop3 /opt/spark
```

```
nano ~/.bashrc
```

Add the env variables:

export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH
export PYSPARK_PYTHON=python3

```
source ~/.bashrc
```

```
sudo apt install python3-pip -y
```

```
pip3 install pyspark
```

```
spark-submit --version
```

![Alt text]()

2. Ensure that you have the crime.csv and offense_codes.csv in the raw-data folder, then run the boston_crime_aggregation.py script using the command:

```
spark-submit boston_crime_aggregation.py --crime_data raw-data/crime.csv --offense_codes raw-data/offense_codes.csv --output_path agg-data/boston_agg_table.parquet
```

3. Read the resulting parquet file that contains aggregation data:

```
spark-submit read_boston_agg.py --agg_data agg-data/boston_agg_table.parquet
```

![Alt text]()