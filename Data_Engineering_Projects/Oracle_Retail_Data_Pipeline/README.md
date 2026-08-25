# 🛒 Oracle Retail Data Pipeline

An end-to-end data engineering and analytics project that integrates an Oracle relational database with Python and Pandas.

The project simulates a retail data environment containing customers, products, orders, and order items. It demonstrates relational database design, SQL-based business analysis, Python/Oracle database integration, transaction management, and a Python data pipeline for extracting, transforming, analyzing, and visualizing data stored in Oracle.

The Oracle database, SQL analysis, and Python/Oracle integration phases are complete. The next phase focuses on extracting Oracle data into Pandas DataFrames for transformation and analysis.

---

# 📁 Project Structure

```text
Oracle_Retail_Data_Pipeline/
├── .env.example
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
    ├── db_connection.py
    ├── transaction_demo.py
    └── exception_handling_demo.py
```

### Directory Overview

| Directory / File | Description |
|---|---|
| `data/` | Exported or generated data files used during the Python analysis phase |
| `notebooks/` | Jupyter notebooks for Pandas analysis and visualization |
| `sql/` | Oracle SQL scripts for schema creation, sample data population, and business analysis |
| `src/` | Python source code for Oracle connectivity, transaction management, and data processing |
| `.env.example` | Example configuration for Oracle database environment variables |

> The actual `.env` file containing database credentials is excluded from version control.

---

# 📌 Project Overview

The project uses a simulated retail database consisting of four related tables:

- `CUSTOMERS` — customer information and signup details
- `PRODUCTS` — product information, categories, and listed prices
- `ORDERS` — customer orders, order dates, and order status
- `ORDER_ITEMS` — products included in each order, quantities, and actual selling prices

The relational structure allows customer purchasing behavior, product performance, revenue trends, discounts, and regional sales patterns to be analyzed.

The project is being developed incrementally to demonstrate the progression from database design and SQL analysis to programmatic database access and Python-based data processing.

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

Additional constraints enforce valid values such as positive quantities and non-negative prices.

---

# 🚀 Project Workflow

| Phase | Description | Status |
|---|---|---|
| 01 | Oracle database schema design | ✅ Completed |
| 02 | Sample retail data population | ✅ Completed |
| 03 | SQL business analysis | ✅ Completed |
| 04 | Python connection to Oracle | ✅ Completed |
| 05 | Oracle data extraction into Pandas | 🚧 In Progress |
| 06 | Data transformation and analysis | ⏳ Planned |
| 07 | Data visualization and reporting | ⏳ Planned |

The overall pipeline is designed as:

```text
Oracle Database
      │
      │ SQL
      ▼
Python / python-oracledb
      │
      ├── Database Connection
      ├── Bind Variables
      ├── Transaction Management
      └── Exception Handling
      │
      ▼
Pandas DataFrames
      │
      ├── Data Validation
      ├── Data Transformation
      ├── Data Merging
      ├── Business Analysis
      └── Feature Creation
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

# 🔌 Python / Oracle Integration

Python is connected directly to the Oracle database using `python-oracledb`.

The integration phase demonstrates programmatic database access and transaction control rather than relying exclusively on SQL Developer.

Implemented features include:

- Oracle database connections from Python
- Cursor creation and management
- SQL execution through Python
- Query result retrieval with:
  - `fetchone()`
  - `fetchmany()`
  - `fetchall()`
  - Cursor iteration
- Bind variables for parameterized SQL
- Python `date` values passed to Oracle `DATE` columns
- `INSERT` and `DELETE` operations
- Explicit transaction control with `COMMIT` and `ROLLBACK`
- Verification of committed data after reconnecting to Oracle
- Transaction rollback verification
- Oracle exception handling
- Safe cursor and connection cleanup
- Environment-based database configuration

---

# 🔄 Transaction Management

`transaction_demo.py` demonstrates Oracle transaction behavior from Python.

The demo includes:

### Rollback Test

```text
INSERT test customer
        │
        ▼
Verify inserted row
        │
        ▼
ROLLBACK
        │
        ▼
Execute SELECT again
        │
        ▼
Verify row no longer exists
```

### Commit Test

```text
INSERT test customer
        │
        ▼
COMMIT
        │
        ▼
Close database connection
        │
        ▼
Reconnect to Oracle
        │
        ▼
Verify committed row still exists
        │
        ▼
Delete test data
        │
        ▼
COMMIT
```

This demonstrates the difference between temporary uncommitted changes and persistent committed database changes.

---

# ⚠️ Exception Handling

`exception_handling_demo.py` demonstrates safe handling of Oracle database errors using:

```text
try
 │
 ├── Connect to Oracle
 └── Execute database operation
        │
        ├── Failure → except → ROLLBACK
        │
        └── Success → else → COMMIT
                              │
                              ▼
                           finally
                              │
                              ├── Close cursor
                              └── Close connection
```

The demo intentionally attempts to insert a duplicate primary key to trigger an Oracle database exception.

The implementation demonstrates:

- `try / except / else / finally`
- `oracledb.Error`
- Transaction rollback after database errors
- Commit after successful operations
- Safe resource cleanup

---

# 🔐 Database Configuration

Database credentials are separated from the Python source code using environment variables.

The local `.env` file contains configuration such as:

```text
ORACLE_USER=...
ORACLE_PASSWORD=...
ORACLE_HOST=...
ORACLE_PORT=...
ORACLE_SERVICE=...
```

Python loads the configuration at runtime rather than hardcoding database credentials in the source code.

The actual `.env` file is excluded from Git using `.gitignore`.

An `.env.example` file is included in the repository to document the required configuration without exposing credentials.

---

# 🐼 Pandas Data Pipeline

The next phase extracts data directly from Oracle into Pandas DataFrames.

Planned tasks include:

- Extracting Oracle query results into DataFrames
- Loading customers, products, orders, and order items
- Inspecting DataFrame structure and data types
- Checking missing values
- Validating extracted data
- Combining relational datasets with `merge()`
- Creating calculated revenue fields
- Performing `groupby()` and aggregation operations
- Reproducing selected SQL analyses using Pandas
- Comparing SQL and Pandas approaches
- Performing additional business analysis
- Creating visualizations
- Exporting analytical results

This phase will build on the existing Python/Oracle connection layer rather than creating a separate data source.

---

# 🛠️ Technologies

## Database

- Oracle Database
- Oracle SQL
- Oracle SQL Developer

## Programming

- Python

## Python Libraries

Current:

- `oracledb`
- `python-dotenv`

Planned for the data analysis phase:

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

### Python & Database Integration

- Python-to-Oracle connectivity
- Database cursors
- SQL execution from Python
- Result-set retrieval
- Bind variables
- Python/Oracle data type integration
- Transaction management
- `COMMIT` and `ROLLBACK`
- Database exception handling
- Connection lifecycle management
- Environment-based configuration
- Secure credential separation

### Data Engineering & Analytics

In Progress / Planned:

- Oracle-to-Pandas data extraction
- DataFrame processing
- Data validation
- Data transformation
- Dataset merging
- Analytical pipelines
- SQL vs. Pandas analysis
- Data visualization
- Result export

---

# 📈 Future Improvements

Future phases of the project will include:

- Oracle-to-Pandas data extraction
- Reusable data extraction functions
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

The project is designed to demonstrate an incremental data engineering workflow:

```text
Database Design
      ↓
Data Population
      ↓
SQL Analysis
      ↓
Python / Oracle Integration
      ↓
Transaction & Error Handling
      ↓
Pandas Data Processing
      ↓
Analysis & Visualization
```

The Oracle SQL and Python/Oracle integration phases are complete.

The project is currently progressing into the Oracle-to-Pandas data extraction and transformation phase.