# Fleximart Data Architecture Project
**Student Name:** Dharani Shridhar
**Student ID:** BITSoM_BA_25071032
**Email:** dharanishridhar29@gmail.com
**Date:** 08/01/2004

This project demonstrates an end-to-end data architecture design for a retail business (Fleximart), This project demonstrates how clean, structured data enables actionable insights for retail decision-making, covering:

## Part 1: Database & ETL
- Raw customer, product, and sales data ingestion
- ETL pipeline using Python
- Data quality checks and reporting
- Relational schema documentation
- Business SQL queries for analytics

## Tech Stack
- Python
- SQL
- MySQL
- Git & GitHub

This project is part of my Business Analytics & Data Management learning journey.

## Project Structure
fleximart-data-architecture/
│
├── part1_database_etl/
│   ├── data/
│   ├── etl_pipeline.py
│   ├── schema.sql
│   ├── business_queries.sql
│   └── data_quality_report.txt
│
├── part2_nosql/
│   ├── products.json
│   ├── mongodb_operations.js
│   └── nosql_analysis.md
│
├── part3_data_warehouse/
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│   └── analytics_queries.sql
│
└── README.md

## Technologies Used

- Python 3.x, pandas, mysql-connector-python
- MySQL 8.0 / PostgreSQL 14
- MongoDB 6.0

1. Navigate to Part 1 (ETL):
- Install Python dependencies (pandas, mysql-connector)
- Run `etl_pipeline.py` to clean and load data

2. SQL scripts can be executed in MySQL Workbench or any SQL client.

3. MongoDB scripts can be run using MongoDB Shell or MongoDB Compass.

4. Data warehouse scripts are designed for analytical querying in a star schema.

## Key Features

- End-to-end ETL pipeline using Python
- Data quality checks and reporting
- Relational database design and business analytics queries
- NoSQL data modeling and MongoDB operations
- Data warehouse design using a star schema
- Analytical SQL queries for business insights

## Key Learnings

- Understanding data architecture as an ecosystem, not silos: Initially, I approached relational databases, NoSQL, and data warehouses as separate tasks. As the project progressed, I realised how decisions made in the ETL layer directly affected downstream analytics and warehouse design. This helped me think more holistically about data flow, consistency, and long-term usability rather than just task completion.
- Importance of data quality over just “making it work”: In the early stages, my focus was on loading data successfully. However, while writing business queries, I noticed inconsistencies and missing values affecting outputs. This pushed me to implement explicit data validation and quality checks, reinforcing that reliable insights depend more on clean data than complex logic.

## Challenges Faced

Challenge: Data inconsistencies and missing values started impacting query outputs during analysis.
Solution: I added explicit data validation and cleaning steps in the ETL process, which improved reliability and made downstream analytics more accurate and trustworthy.

Challenge: Initial schema designs were technically correct but not optimised for analytical queries.
Solution: I reworked the models into a clearer star schema structure, focusing on business use cases and query efficiency rather than just database normalization.


