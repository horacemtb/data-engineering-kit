## Analyze Provided ER Model

Identify primary keys (PK), foreign keys (FK), and attributes in the four operational tables (Person, Manager, Department, Company).

## Stage 1: Staging Area (STG)

Copy data from the source system without modifications.

- Write SQL queries to extract data with necessary metadata.
- Draw the resulting ER model.

## Stage 2: Dimensional Data Store (DDS)

Transform STG data before loading into the Data Warehouse.

- Perform Data Vault operations:

-- select business keys;
-- create hash of business keys;
-- add technical data (source, load timestamp);
-- create link tables;
-- create hub tables;
-- create satellite tables.

- Write SQL queries for creating hubs, links, and satellites.
- Draw the resulting ER model.

## Stage 3: Common Data Mart (CDM)

Prepare data for visualization.

- Write SQL queries to implement metrics for department manager count and employee count.
- Draw the resulting ER model.

## Results

All the ER models and SQL queries can be found in the corresponding folders. 