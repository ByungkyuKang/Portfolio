# Week 05 — Pandas Basics

## Overview

This week focuses on learning the basics of pandas and understanding how to work with DataFrames.

The goal is to learn how to create, inspect, and understand tabular data using pandas.

Pandas is an important Python library for data analysis, machine learning, and data engineering because it provides powerful tools for working with structured data.

---

## Day 01 — Pandas Installation and DataFrame Creation

### Topics Covered

- Understanding what pandas is
- Importing pandas with `import pandas as pd`
- Checking the pandas version
- Understanding what a DataFrame is
- Creating a DataFrame from a dictionary
- Creating a DataFrame from a list of dictionaries
- Creating a DataFrame with custom index labels
- Understanding rows, columns, and index
- Inspecting DataFrames with `head()`
- Checking DataFrame shape with `shape`
- Checking column names with `columns`
- Checking data types with `dtypes`
- Checking DataFrame information with `info()`

### Practice File

| File | Description |
|---|---|
| [Day_01_Pandas_Installation_DataFrame_Creation.ipynb](./Day_01_Pandas_Installation_DataFrame_Creation.ipynb) | Practice notebook for importing pandas, creating basic DataFrames, using custom index labels, and inspecting DataFrame information |

### Practice Summary

In this notebook, I practiced creating and inspecting basic pandas DataFrames.

The practice includes:

- Checking the installed pandas version
- Creating a simple DataFrame from a dictionary
- Creating a DataFrame from a list of dictionaries
- Creating a DataFrame with custom index labels
- Inspecting a DataFrame using `head()`, `shape`, `columns`, `dtypes`, and `info()`
- Creating an employee DataFrame using work-related sample data

---

## Day 02 — Read CSV Files with pandas

### Topics Covered

- Understanding what a CSV file is
- Creating sample CSV files with `to_csv()`
- Reading CSV files with `pd.read_csv()`
- Understanding file paths for CSV files
- Checking whether a CSV file exists with `os.path.exists()`
- Inspecting loaded DataFrames with `head()`, `shape`, `columns`, `dtypes`, and `info()`
- Reading selected columns with `usecols`
- Reading a limited number of rows with `nrows`
- Saving and loading simple practice datasets

### Practice File

| File | Description |
|---|---|
| [Day_02_Read_CSV_Files.ipynb](./Day_02_Read_CSV_Files.ipynb) | Practice notebook for creating and reading CSV files with pandas |

### Generated CSV Files

| File | Description |
|---|---|
| [students.csv](../assets/Week05/Day02/Output/students.csv) | Sample student dataset created and read during CSV practice |
| [model_results.csv](../assets/Week05/Day02/Output/model_results.csv) | Sample model results dataset created and read during CSV practice |

---

## Day 03 — Select Columns in pandas

### Topics Covered

- Loading CSV files into pandas DataFrames
- Checking available column names with `df.columns`
- Converting column names to a list
- Selecting one column with `df["column_name"]`
- Understanding that a single selected column returns a Series
- Selecting one column as a DataFrame with `df[["column_name"]]`
- Selecting multiple columns with `df[["column1", "column2"]]`
- Storing selected columns in variables
- Calculating simple statistics from selected numeric columns
- Using `mean()`, `max()`, and `min()` on selected columns
- Understanding that incorrect column names can cause a `KeyError`
- Selecting columns from multiple CSV-based DataFrames

### Practice File

| File | Description |
|---|---|
| [Day_03_Select_Columns.ipynb](./Day_03_Select_Columns.ipynb) | Practice notebook for selecting single and multiple columns from pandas DataFrames |

### Related Input Files

| File | Description |
|---|---|
| [students.csv](../assets/Week05/Day03/Input/students.csv) | Student dataset used to practice column selection and basic numeric column calculations |
| [model_results.csv](../assets/Week05/Day03/Input/model_results.csv) | Model result dataset used to practice selecting model and accuracy columns |

---

## Day 04 — Row Filtering in pandas

### Topics Covered

- Creating a sample CSV file for row filtering practice
- Reading CSV files into pandas DataFrames
- Filtering rows with numeric conditions
- Filtering rows with string conditions
- Filtering rows with boolean columns
- Creating boolean conditions from DataFrame columns
- Filtering rows with multiple conditions using `&`
- Filtering rows with OR conditions using `|`
- Filtering rows with `isin()`
- Filtering rows with `between()`
- Filtering rows and selecting columns together using `.loc[]`
- Understanding common filtering mistakes such as using `and` / `or` instead of `&` / `|`

### Practice File

| File | Description |
|---|---|
| [Day_04_Row_Filtering.ipynb](./Day_04_Row_Filtering.ipynb) | Practice notebook for filtering rows in pandas DataFrames using conditions, multiple conditions, `isin()`, `between()`, and `.loc[]` |

### Related Input Files

| File | Description |
|---|---|
| [students.csv](../assets/Week05/Day04/Input/students.csv) | Student dataset created and used for row filtering practice |

---

## Weekly Summary

This week focuses on learning pandas basics for data analysis, machine learning, and data engineering.

So far, I practiced how to:

- Import pandas using the standard alias `pd`
- Check the installed pandas version
- Understand the basic structure of a DataFrame
- Create DataFrames from dictionaries
- Create DataFrames from lists of dictionaries
- Create DataFrames with custom index labels
- Inspect DataFrames using `head()`, `shape`, `columns`, `dtypes`, and `info()`
- Create simple DataFrames using personal, model, skill, and employee sample data
- Understand what CSV files are
- Create CSV files from DataFrames using `to_csv()`
- Read CSV files into DataFrames using `pd.read_csv()`
- Check file paths before reading CSV files
- Read selected columns using `usecols`
- Read a limited number of rows using `nrows`
- Check available column names before selecting columns
- Select a single column as a Series
- Select a single column as a DataFrame
- Select multiple columns as a DataFrame
- Store selected columns in variables
- Calculate simple statistics from selected numeric columns
- Understand that incorrect column names can cause a `KeyError`
- Filter rows using numeric, string, and boolean conditions
- Combine multiple filtering conditions using `&` and `|`
- Use `isin()` to filter rows by multiple possible values
- Use `between()` to filter rows within a numeric range
- Use `.loc[]` to filter rows and select columns at the same time

These concepts are important foundations for working with structured data in future data analysis, machine learning, and data engineering projects.