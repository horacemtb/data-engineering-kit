This project uses supermarket sales data from:

https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales

1. Deploy PostgreSQL and Metabase containers using Docker Compose:

```
docker-compose up -d
```

2. Access the Postgres container with the following command:

```
docker exec -it postgres psql -U metabase -d metabase_db
```

3. Execute the following SQL queries:

- metabase-bi/sql_queries/create_table.sql
- metabase-bi/sql_queries/insert_data.sql

4. Access the Metabase UI at http://localhost:3000/

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/metabase-bi/images/1.%20Access%20Metabase.png)

5. Configure the connection with the Postgres instance. You should now see the supermarket sales table in the UI:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/metabase-bi/images/2.%20Check%20the%20table.png)

6. Build a few charts and tables, then save them in your personal collection:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/metabase-bi/images/3.%20Collection.png)

7. The dashboard will look like the following:

- The first section shows key performance metrics such as total revenue, average rating, number of units sold, and a bar chart of revenue grouped by item category:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/metabase-bi/images/4.%20Dashboard%20screenshot%201.png)

- The second section displays a time series showing the number of units sold on a weekly basis:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/metabase-bi/images/5.%20Dashboard%20screenshot%202.png)

- The third section contains a pie chart for revenue by payment method, two pivot tables for units sold and average bill by customer type and gender, and a general table showing total sales by product line, city, and branch:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/metabase-bi/images/6.%20Dashboard%20screenshot%203.png)

- The dashboard includes three filters to sort data by city, branch, and time (month/year). The example below shows the filters in action:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/metabase-bi/images/7.%20Filter%20example%201.png)
![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/metabase-bi/images/8.%20Filter%20example%202.png)

- Each plot or table also includes a short explanation, visible by hovering over the "i" icon.

8. The entire dashboard has also been saved and exported as a PDF for reference.