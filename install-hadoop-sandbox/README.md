1. Create a Docker alias for the Docker command to pull and run Hortonworks Hadoop Sandbox image:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/installation/1.%20Add%20Docker%20alias%20and%20pull%20and%20run%20hortonworks%20sandbox%20image.png)

2. Check Ambari server status:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/installation/2.%20Ambari%20server%20status.png)

3. Reset Ambari admin password

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/installation/3.%20Reset%20ambari%20password.png)

4. From the Ambari UI start the required services HDFS, YARN, Hive, Spark2, Zeppelin Notebook, Data Analytics Studio, ZooKeeper, MapReduce2, Oozie, Kafka, Ranger, Atlas:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/installation/4.%20Start%20services.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/installation/5.%20Start%20services%202.png)

5. Ensure that the services are running:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/installation/6.%20Services%20running.png)

6. Open Zeppelin Notebook and use a toy pyspark example to ensure the service is running:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/installation/7.%20Run%20zeppelin%20notebook.png)

7. Open DAS and use a simple query to ensure the service is running:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/installation/8.%20Run%20data%20analytics%20studio.png)

