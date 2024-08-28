1. Create two virtual machines: one with Airflow installed and the other to run a PostgreSQL database using Docker:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/airflow-postgresql/images/1.Create%20two%20VMs.png)

2. Connect to the main VM and run the following commands to start a PostgreSQL database and create a table::

```
docker run --name analytics-db -e POSTGRES_PASSWORD=... -e POSTGRES_DB=analytics -d -p 5432:5432 postgres 
```

```
docker exec -it analytics-db psql -U postgres -d analytics
```

```
CREATE TABLE iss_position (
    timestamp BIGINT PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT
);
```

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/airflow-postgresql/images/2.Create%20a%20table%20iss_position.png)

3. Connect to the Airflow VM, navigate to the Airflow UI, and configure a database connection:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/airflow-postgresql/images/3.Create%20Connection.png)

4. Write the DAG code for loading and inserting data, and place it in the specified folder:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/airflow-postgresql/images/4.Write%20DAG%20code.png)

The complete code can be found at airflow-postgresql/iss_position_dag.py

5. Run the DAG via the Airflow UI and wait for it to complete at least five runs. You should see green circles indicating successful execution:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/airflow-postgresql/images/5.1.Successful%20DAG%20runs.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/airflow-postgresql/images/5.2.Successful%20DAG%20runs.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/airflow-postgresql/images/5.3.DAG%20graph.png)

6. Check the task logs to ensure they have completed successfully and without errors:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/airflow-postgresql/images/6.1.Log%20example%201.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/airflow-postgresql/images/6.2.Log%20example%202.png)

7. Connect to the main VM and verify that the data has been successfully inserted into the database:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/airflow-postgresql/images/7.DB%20entries.png)