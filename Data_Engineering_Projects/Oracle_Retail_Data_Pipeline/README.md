# 🛒 Oracle Retail Data Pipeline

An end-to-end data engineering and analytics project that integrates an Oracle relational database with Python, SQLAlchemy, and Pandas.

The project simulates a retail data environment containing customers, products, orders, and order items. It demonstrates relational database design, SQL-based business analysis, Python/Oracle database integration, transaction management, data extraction, data quality validation, and transformation of relational data into analysis-ready datasets.

The Oracle database, SQL analysis, Python/Oracle integration, Oracle-to-Pandas extraction, and data validation phases are complete. The project is currently progressing through the data transformation phase.

---

# 📁 Project Structure

```text
Oracle_Retail_Data_Pipeline/
├── .env.example
├── README.md
├── requirements.txt
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
    ├── extract_data.py
    ├── validate_data.py
    ├── transform_data.py
    ├── main.py
    ├── transaction_demo.py
    └── exception_handling_demo.py
```

### Directory Overview

| Directory / File | Description |
|---|---|
| `data/` | Exported or generated analytical datasets |
| `notebooks/` | Jupyter notebooks for analysis and visualization |
| `sql/` | Oracle SQL scripts for schema creation, sample data population, and business analysis |
| `src/db_connection.py` | Oracle DBAPI connection and SQLAlchemy engine configuration |
| `src/extract_data.py` | Reusable Oracle-to-Pandas data extraction |
| `src/validate_data.py` | Data quality and relational integrity validation |
| `src/transform_data.py` | Transformation of extracted relational data into analysis-ready datasets |
| `src/main.py` | Main pipeline orchestration |
| `src/transaction_demo.py` | Oracle transaction behavior demonstration |
| `src/exception_handling_demo.py` | Database exception handling demonstration |
| `.env.example` | Example Oracle database environment configuration |
| `requirements.txt` | Python project dependencies |

> The actual `.env` file containing database credentials is excluded from version control.

---

# 📌 Project Overview

The project uses a simulated retail database consisting of four related tables:

- `CUSTOMERS` — customer information and signup details
- `PRODUCTS` — product information, categories, and listed prices
- `ORDERS` — customer orders, order dates, and order status
- `ORDER_ITEMS` — products included in each order, quantities, and historical selling prices

The relational structure allows customer purchasing behavior, product performance, revenue trends, discounts, and regional sales patterns to be analyzed.

The project is developed incrementally to demonstrate a complete workflow from relational database design and SQL analysis to programmatic extraction, validation, transformation, and analytics.

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

Primary and foreign key constraints maintain referential integrity between the tables.

Additional constraints enforce business rules such as:

- Product prices must be non-negative
- Order item quantities must be greater than zero
- Order item unit prices must be non-negative
- Order status must be one of:
  - `PENDING`
  - `SHIPPED`
  - `COMPLETED`
  - `CANCELLED`

---

# 🚀 Project Workflow

| Phase | Description | Status |
|---|---|---|
| 01 | Oracle database schema design | ✅ Completed |
| 02 | Sample retail data population | ✅ Completed |
| 03 | SQL business analysis | ✅ Completed |
| 04 | Python connection to Oracle | ✅ Completed |
| 05 | Oracle data extraction into Pandas | ✅ Completed |
| 06 | Data quality validation | ✅ Completed |
| 07 | Data transformation | 🚧 In Progress |
| 08 | Analytical dataset generation | ⏳ Planned |
| 09 | Data visualization and reporting | ⏳ Planned |

The current pipeline architecture is:

```text
Oracle Database
      │
      ▼
Data Extraction
(extract_data.py)
      │
      ▼
Pandas DataFrames
      │
      ▼
Data Validation
(validate_data.py)
      │
      ├── Primary Key Duplicate Checks
      ├── Constraint Validation
      └── Foreign Key Integrity Checks
      │
      ▼
Data Transformation
(transform_data.py)
      │
      ├── Relational Dataset Merging
      ├── Revenue Field Creation
      ├── Order-Level Calculations
      └── Date Feature Creation
      │
      ▼
Analysis-Ready Datasets
      │
      ▼
Analysis / Visualization / Reporting
```

`main.py` acts as the orchestration layer that coordinates the extraction, validation, and transformation stages.

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
- Completed, cancelled, pending, and shipped orders
- Orders containing multiple products
- Historical selling prices that may differ from current listed prices
- Customers with different purchasing behaviors

The dataset is intentionally structured to support realistic SQL analysis and data engineering scenarios.

---

## 03. `03_analysis_queries.sql`

Contains business-oriented SQL queries ranging from basic filtering to analytical SQL.

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

These questions simulate common analytical tasks performed against transactional business data.

---

# 🔌 Python / Oracle Integration

Python connects directly to Oracle using `python-oracledb`.

SQLAlchemy is additionally used to provide a database engine for Pandas-based data extraction.

Implemented features include:

- Oracle database connections from Python
- Reusable database connection functions
- SQLAlchemy engine creation
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

# 📥 Oracle-to-Pandas Data Extraction

Oracle data is extracted into Pandas DataFrames using reusable extraction logic in `extract_data.py`.

The pipeline currently extracts:

- `CUSTOMERS`
- `PRODUCTS`
- `ORDERS`
- `ORDER_ITEMS`

The extraction layer includes:

- SQLAlchemy-based Oracle connectivity for Pandas
- Reusable table extraction
- Table-name validation using an allowlist
- Deterministic ordering by primary key
- DataFrame structure inspection
- Column and data type inspection
- Missing-value inspection
- Extraction error handling

This keeps database access logic separate from validation and transformation logic.

---

# ✅ Data Quality Validation

`validate_data.py` validates extracted DataFrames before transformation.

The validation layer currently performs three categories of checks.

### Primary Key Validation

Checks for duplicate primary keys in:

- `CUSTOMERS`
- `PRODUCTS`
- `ORDERS`
- `ORDER_ITEMS`

### Constraint Validation

Validates business rules including:

- `PRODUCTS.PRICE >= 0`
- `ORDER_ITEMS.QUANTITY > 0`
- `ORDER_ITEMS.UNIT_PRICE >= 0`
- Valid `ORDERS.STATUS` values

### Foreign Key Integrity

Checks that:

```text
ORDERS.CUSTOMER_ID
        → CUSTOMERS.CUSTOMER_ID

ORDER_ITEMS.ORDER_ID
        → ORDERS.ORDER_ID

ORDER_ITEMS.PRODUCT_ID
        → PRODUCTS.PRODUCT_ID
```

Validation results are collected into a structured result object and used to calculate the total number of detected violations.

The pipeline reports an overall validation result:

```text
Total Violations: 0
Overall Validation: PASS
```

or:

```text
Total Violations: N
Overall Validation: FAIL
```

Validation logic operates on DataFrames independently from the Oracle connection layer, keeping data quality checks separate from extraction.

---

# 🔄 Data Transformation

`transform_data.py` transforms the validated relational DataFrames into an analysis-ready order detail dataset.

The current transformation combines:

```text
ORDERS
   │
   ├── CUSTOMER_ID
   ▼
CUSTOMERS
   │
   │
   ├── ORDER_ID
   ▼
ORDER_ITEMS
   │
   ├── PRODUCT_ID
   ▼
PRODUCTS
```

The resulting `order_details_df` uses an **order-item grain**:

> One row represents one product line within an order, enriched with order, customer, and product information.

Current transformations include:

### Revenue per Order Line

```text
line_total = quantity × unit_price
```

The historical `unit_price` stored in `ORDER_ITEMS` is used rather than the current product list price.

### Order Total

Order-level revenue is calculated from all line items belonging to the same order while preserving the detailed order-item rows.

Conceptually:

```sql
SUM(line_total) OVER (PARTITION BY order_id)
```

### Date Features

The transformation layer currently derives:

- `order_year`
- `order_month`
- `order_year_month`

These fields support later time-based aggregation and monthly revenue analysis.

---

# 🧱 Pipeline Design

The Python code follows separation of concerns across pipeline stages:

```text
db_connection.py
        │
        │ Database connectivity
        ▼
extract_data.py
        │
        │ Oracle → DataFrames
        ▼
validate_data.py
        │
        │ Data quality checks
        ▼
transform_data.py
        │
        │ DataFrames → analysis-ready dataset
        ▼
main.py
        │
        │ Pipeline orchestration
        ▼
Analysis / Reporting
```

This structure keeps database access, validation, transformation, and pipeline control logically separated.

---

# 🛠️ Technologies

## Database

- Oracle Database
- Oracle SQL
- Oracle SQL Developer

## Programming

- Python

## Python Libraries

Current project dependencies include:

- `oracledb`
- `pandas`
- `python-dotenv`
- `SQLAlchemy`

## Development Tools

- VS Code
- Git
- GitHub
- Jupyter Notebook

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
- SQLAlchemy database engine configuration

### Data Engineering & Analytics

Implemented:

- Oracle-to-Pandas data extraction
- Reusable extraction logic
- DataFrame inspection
- Primary key duplicate validation
- Business constraint validation
- Foreign key integrity validation
- Multi-table DataFrame merging
- Calculated revenue fields
- Window-style calculations with Pandas `transform()`
- Date feature engineering
- Modular pipeline organization

In Progress / Planned:

- Order-level analytical datasets
- Customer-level analytical datasets
- Product-level analytical datasets
- Pandas-based business analysis
- SQL vs. Pandas analysis comparison
- Business KPI generation
- Data visualization
- Analytical result export

---

# 📈 Future Improvements

Future phases of the project will include:

- Order-level summary dataset generation
- Customer-level summary dataset generation
- Product-level summary dataset generation
- Business KPI generation
- Pandas-based business analysis
- SQL vs. Pandas analysis comparisons
- Data visualization
- CSV analytical result exports
- Additional pipeline validation and error handling
- Further pipeline modularization where appropriate

---

# 📝 Notes

This project uses simulated retail data created specifically for learning and portfolio purposes.

The project demonstrates an incremental data engineering workflow:

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
Oracle-to-Pandas Extraction
      ↓
Data Quality Validation
      ↓
Data Transformation
      ↓
Analysis-Ready Datasets
      ↓
Analysis & Visualization
```

The Oracle SQL, Python/Oracle integration, Oracle-to-Pandas extraction, and data validation phases are complete.

The project is currently progressing through the transformation of validated relational data into analysis-ready datasets.