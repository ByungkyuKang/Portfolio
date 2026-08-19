# 🛒 Oracle Retail Data Pipeline

An end-to-end data engineering and analytics project that integrates an Oracle relational database with Python and Pandas.

The project simulates a retail data environment containing customers, products, orders, and order items. It demonstrates relational database design, SQL-based business analysis, and a Python data pipeline for extracting, transforming, analyzing, and visualizing data stored in Oracle.

The Oracle database and SQL analysis phase is complete. Python/Oracle integration and Pandas-based data processing will be developed in the next phase.

---

# 📁 Project Structure

```text
Oracle_Retail_Data_Pipeline/
├── README.md
│
├── data/
│
├── notebooks/
│
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_populate_tables.sql
│   └── 03_analysis_queries.sql
│
└── src/
```

### Directory Overview

| Directory | Description |
|---|---|
| `data/` | Exported or generated data files used during the Python analysis phase |
| `notebooks/` | Jupyter notebooks for Pandas analysis and visualization |
| `sql/` | Oracle SQL scripts for schema creation, sample data population, and business analysis |
| `src/` | Python source code for Oracle connectivity and data processing |

---

# 📌 Project Overview

The project uses a simulated retail database consisting of four related tables:

- `CUSTOMERS` — customer information and signup details
- `PRODUCTS` — product information, categories, and listed prices
- `ORDERS` — customer orders, order dates, and order status
- `ORDER_ITEMS` — products included in each order, quantities, and actual selling prices

The relational structure allows customer purchasing behavior, product performance, revenue trends, discounts, and regional sales patterns to be analyzed.

---

# 🗄️ Database Schema

The Oracle database contains the following relationships:

```text
CUSTOMERS
    │
    │ 1 : N
    ▼
ORDERS
    │
    │ 1 : N
    ▼
ORDER_ITEMS
    │
    │ N : 1
    ▼
PRODUCTS
```

Primary and foreign key constraints are used to maintain referential integrity between the tables.

Additional constraints are used to enforce valid values such as positive quantities and non-negative prices.

---

# 🚀 Project Workflow

| Phase | Description | Status |
|---|---|---|
| 01 | Oracle database schema design | ✅ Completed |
| 02 | Sample retail data population | ✅ Completed |
| 03 | SQL business analysis | ✅ Completed |
| 04 | Python connection to Oracle | 🚧 Planned |
| 05 | Oracle data extraction into Pandas | 🚧 Planned |
| 06 | Data transformation and analysis | 🚧 Planned |
| 07 | Data visualization and reporting | 🚧 Planned |

The overall pipeline is designed as:

```text
Oracle Database
      │
      │ SQL
      ▼
Python / python-oracledb
      │
      ▼
Pandas DataFrames
      │
      ├── Data validation
      ├── Data transformation
      ├── Data merging
      ├── Business analysis
      └── Feature creation
      │
      ▼
Visualization / Reporting
```

---

# 📄 SQL Scripts

## 01. `01_create_tables.sql`

Creates the relational database schema used by the project.

The script creates:

- `CUSTOMERS`
- `PRODUCTS`
- `ORDERS`
- `ORDER_ITEMS`

The schema includes:

- Primary keys
- Foreign keys
- `NOT NULL` constraints
- `CHECK` constraints
- Relational integrity between customers, orders, order items, and products

---

## 02. `02_populate_tables.sql`

Populates the database with simulated retail transaction data.

The sample dataset contains:

- Customers from multiple U.S. states
- Products across multiple categories
- Customer orders across multiple months
- Completed, cancelled, and pending orders
- Orders containing multiple products
- Historical selling prices that may differ from current listed prices
- Customers with different purchasing behaviors

The dataset is intentionally structured to support realistic SQL analysis scenarios.

---

## 03. `03_analysis_queries.sql`

Contains business-oriented SQL queries ranging from basic filtering to analytical SQL.

The analysis includes:

### Basic Queries

- Completed order retrieval
- Customer filtering by state

### JOIN Operations

- Orders with customer information
- Detailed order item information

### Aggregation

- Order count per customer
- Revenue by product
- Revenue by product category
- Monthly revenue
- Revenue by state

### Customer Analysis

- Customers with no orders
- Repeat customers
- Customer spending classification
- Highest-spending customer
- Top customer by state

### Product Analysis

- Products with above-average revenue
- Product revenue ranking
- Product ranking within each category
- Discounted sales analysis

### Analytical SQL

The project uses several intermediate and advanced Oracle SQL techniques, including:

- `INNER JOIN`
- `LEFT JOIN`
- `NOT EXISTS`
- `GROUP BY`
- `HAVING`
- `CASE`
- Common Table Expressions (`WITH`)
- Subqueries
- `FETCH FIRST`
- `RANK()`
- `ROW_NUMBER()`
- `PARTITION BY`
- `LAG()`
- Date aggregation with `TO_CHAR()`

---

# 📊 Business Questions

The SQL analysis answers questions such as:

- Which products generate the most revenue?
- Which product categories generate the most sales?
- Which customers spend the most?
- Which customers repeatedly place orders?
- How does revenue change from month to month?
- Which products generate above-average revenue?
- Which products rank highest within their category?
- Which states generate the most revenue?
- Who is the highest-spending customer in each state?
- Which products were sold below their listed price?

These questions are designed to simulate common analytical tasks performed against transactional business data.

---

# 🐍 Python / Pandas Phase

The next phase will connect Python directly to the Oracle database using `python-oracledb`.

Oracle tables will be extracted into Pandas DataFrames for further processing and analysis.

Planned tasks include:

- Establishing an Oracle database connection from Python
- Executing SQL queries from Python
- Loading Oracle query results into Pandas DataFrames
- Inspecting data types and missing values
- Validating extracted data
- Combining datasets using Pandas `merge()`
- Creating calculated revenue fields
- Performing `groupby()` and aggregation operations
- Reproducing selected SQL analyses with Pandas
- Performing additional business analysis
- Creating visualizations
- Exporting analytical results

This phase will demonstrate how SQL-based relational data can be integrated into a Python data analysis workflow.

---

# 🛠️ Technologies

## Database

- Oracle Database
- Oracle SQL
- Oracle SQL Developer

## Programming

- Python

## Python Libraries

Planned for the Python phase:

- `oracledb`
- `pandas`
- `NumPy`
- `matplotlib`

## Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

---

# 💡 Skills Demonstrated

### Database & SQL

- Relational database design
- Primary and foreign key relationships
- Database constraints
- Data population
- SQL filtering
- Multi-table joins
- Aggregation
- Subqueries
- Common Table Expressions
- Analytical/window functions
- Ranking
- Time-based analysis
- Business-oriented SQL analysis

### Python & Data Engineering

Planned:

- Oracle/Python database connectivity
- SQL data extraction
- Pandas DataFrame processing
- Data validation
- Data transformation
- Dataset merging
- Analytical pipelines
- Data visualization
- Result export

---

# 📈 Future Improvements

Future phases of the project will include:

- Python-to-Oracle database integration
- Pandas-based data transformation
- SQL vs. Pandas analysis comparisons
- Automated data extraction
- Data quality validation
- Business KPI generation
- Data visualization
- CSV result exports
- Improved pipeline modularization

---

# 📝 Notes

This project uses simulated retail data created specifically for learning and portfolio purposes.

The project is designed to demonstrate the progression from relational database design and SQL analysis to Python-based data extraction and transformation.

The Oracle SQL phase is complete, while the Python/Pandas pipeline is currently under development.