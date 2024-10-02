COPY supermarket_sales (InvoiceID, Branch, City, CustomerType, Gender, ProductLine, UnitPrice, Quantity, Tax, Total, Date, Time, Payment, COGS, GrossMarginPercentage, GrossIncome, Rating)
FROM '/var/lib/postgresql/data/supermarket_sales_.csv' 
DELIMITER ',' 
CSV;
