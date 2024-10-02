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

![Alt text]()

5. Configure the connection with the Postgres instance. You should now see the supermarket sales table in the UI:

![Alt text]()

6. Build a few charts and tables, then save them in your personal collection:

![Alt text]()

7. The dashboard will look like the following:

- The first section shows key performance metrics such as total revenue, average rating, number of units sold, and a bar chart of revenue grouped by item category:

![Alt text]()

- The second section displays a time series showing the number of units sold on a weekly basis:

![Alt text]()

- The third section contains a pie chart for revenue by payment method, two pivot tables for units sold and average bill by customer type and gender, and a general table showing total sales by product line, city, and branch:

![Alt text]()

- The dashboard includes three filters to sort data by city, branch, and time (month/year). The example below shows the filters in action:

![Alt text]()
![Alt text]()

- Each plot or table also includes a short explanation, visible by hovering over the "i" icon.

8. The entire dashboard has also been saved and exported as a PDF for reference.