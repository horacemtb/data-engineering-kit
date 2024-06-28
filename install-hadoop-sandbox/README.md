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

8. Create a table called employee, verify that it exists and fill it with data:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/test-table/1.%20Create%20employee%20table.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/test-table/2.%20Verify%20employee%20table.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/test-table/3.%20Populate%20employee%20table.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/test-table/4.%20Check%20filled%20employee%20table.png)

9. Launch the Ranger service to configure access policies for users:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/create-range-resource-based-policy/1.%20Start%20Ranger.png)

10. Configure a resource-based policy that prevents the raj_obs and maria_dev users from accessing the ssn and location columns of the employee table.

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/create-range-resource-based-policy/2.%20Configure%20resource-based%20policy.png)

11. Check that maria_dev can't access all of the columns of the employee table:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/create-range-resource-based-policy/3.%20Check%20that%20maria_dev%20can't%20access%20all%20of%20the%20columns.png)

12. Go to Ranger Audit and check the event:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/create-range-resource-based-policy/4.%20User%20maria_dev%20denied.png)

13. Next, configure a tag-based policy. Open the Atlas service and create a new classification:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/create-atlas-tag/1.%20Atlas%20create%20classification.png)

14. Find the employee table using Atlas search:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/create-atlas-tag/2.%20Atlas%20see%20table%20properties%20and%20schema.png)

15. Add tags to the columns:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/create-atlas-tag/3.%20Atlas%20add%20tags.png)

16. Next, go to the Ranger Tag section:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/create-ranger-tag-based-policy/1.%20Ranger%20add%20Sandbox_tag.png)

17. Add and configure a tag-based policy for the raj_ops user:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/create-ranger-tag-based-policy/2.%20Ranger%20add%20tag_based%20policy%20for%20raj_ops.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/create-ranger-tag-based-policy/3.%20Ranger%20enable%20Sandbox_tag.png)

18. Check that raj_ops has access to the whole table:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/install-hadoop-sandbox/images/create-ranger-tag-based-policy/4.%20Check%20that%20raj_ops%20has%20access.png)
