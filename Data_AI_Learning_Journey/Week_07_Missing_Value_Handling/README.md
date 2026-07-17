# Week 07 — Missing Value Handling

## Overview

This week focuses on handling missing values in pandas.

The goal is to learn how to identify, inspect, summarize, and later handle missing values such as `NaN`.

Missing value handling is an important part of data cleaning because incomplete data can affect analysis results, reports, and machine learning models.

---

## Day 01 — Checking Missing Values with isnull()

### Topics Covered

- Understanding missing values in pandas
- Understanding `NaN`
- Creating a sample employee dataset with missing values
- Saving a DataFrame as a CSV file using `to_csv()`
- Reading a CSV file using `pd.read_csv()`
- Checking missing values with `isnull()`
- Understanding Boolean results from `isnull()`
- Counting missing values by column using `isnull().sum()`
- Counting total missing values using `isnull().sum().sum()`
- Calculating missing value percentages using `isnull().mean()`
- Filtering rows that contain at least one missing value using `any(axis=1)`
- Counting missing values by row using `sum(axis=1)`
- Creating a temporary `Missing_Value_Count` column
- Checking missing values in specific columns
- Extracting complete rows using `notnull().all(axis=1)`
- Checking whether a DataFrame contains any missing values using `any().any()`
- Creating a missing value summary DataFrame
- Creating a summary containing only columns with missing values
- Saving missing value summary results as CSV files
- Understanding why `== None` should not be used to check missing values
- Understanding that empty strings are not always treated as missing values

### Practice File

| File | Description |
|---|---|
| [Day_01_Check_Missing_Values_IsNull.ipynb](./Day_01_Check_Missing_Values_IsNull.ipynb) | Practice notebook for checking and summarizing missing values in pandas using `isnull()` |

### Input File

| File | Description |
|---|---|
| [employee_data_with_missing_values.csv](../assets/Week07/Day01/Input/employee_data_with_missing_values.csv) | Sample employee dataset containing missing values for missing value analysis practice |

### Output Files

| File | Description |
|---|---|
| [missing_value_summary.csv](../assets/Week07/Day01/output/missing_value_summary.csv) | CSV file containing missing value counts and percentages for all columns |
| [rows_with_missing_values.csv](../assets/Week07/Day01/output/rows_with_missing_values.csv) | CSV file containing rows that have at least one missing value |
| [missing_values_only.csv](../assets/Week07/Day01/output/missing_values_only.csv) | CSV file containing only columns that have missing values |

### Practice Summary

In this notebook, I practiced checking missing values in pandas using `isnull()`.

The practice includes:

- Creating a dataset with missing values
- Checking missing value locations
- Counting missing values by column
- Counting total missing values
- Calculating missing value percentages
- Finding rows with missing values
- Counting missing values by row
- Checking missing values in specific columns
- Finding complete rows with no missing values
- Creating missing value summary DataFrames
- Saving missing value summary results as CSV files

This practice helped me understand how to inspect missing data before deciding whether to remove, fill, or transform missing values.

---

## Day 02 — Filling Missing Values with fillna()

### Topics Covered

- Understanding how to fill missing values in pandas
- Understanding `fillna()`
- Creating a sample employee dataset with missing values
- Saving a DataFrame as a CSV file using `to_csv()`
- Reading a CSV file using `pd.read_csv()`
- Checking missing values before filling them
- Filling missing categorical values with fixed values
- Filling missing numeric values with the mean
- Filling missing numeric values with the median
- Filling missing categorical values with the mode
- Understanding why `mode()[0]` is used
- Filling missing boolean values with `False`
- Handling boolean columns safely with nullable boolean dtype
- Filling different columns with different values using a dictionary
- Checking missing values again after using `fillna()`
- Counting total missing values after filling
- Creating a before-and-after missing value summary DataFrame
- Understanding that `fillna()` does not permanently modify the original DataFrame unless the result is assigned back
- Understanding why using one fill value for all columns can be dangerous
- Applying `fillna()` concepts to a separate customer orders practice dataset
- Creating a new column after filling missing values
- Saving filled datasets and fillna summary results as CSV files

### Practice File

| File | Description |
|---|---|
| [Day_02_Fill_Missing_Values_Fillna.ipynb](./Day_02_Fill_Missing_Values_Fillna.ipynb) | Practice notebook for filling missing values in pandas using `fillna()` |

### Input File

| File | Description |
|---|---|
| [employee_data_with_missing_values.csv](../assets/Week07/Day02/Input/employee_data_with_missing_values.csv) | Sample employee dataset containing missing values for fillna practice |

### Output Files

| File | Description |
|---|---|
| [employee_data_filled.csv](../assets/Week07/Day02/Output/employee_data_filled.csv) | CSV file containing the employee dataset after missing values were filled |
| [fillna_summary.csv](../assets/Week07/Day02/Output/fillna_summary.csv) | CSV file comparing missing value counts before and after using `fillna()` |
| [customer_orders_filled.csv](../assets/Week07/Day02/Output/customer_orders_filled.csv) | Practice CSV file containing the cleaned customer orders dataset |
| [customer_orders_fillna_summary.csv](../assets/Week07/Day02/Output/customer_orders_fillna_summary.csv) | Practice CSV file comparing missing value counts before and after filling the customer orders dataset |

### Practice Summary

In this notebook, I practiced filling missing values in pandas using `fillna()`.

The practice includes:

- Filling missing categorical values with fixed values such as `"Unknown"`
- Filling numeric columns with calculated values such as mean and median
- Filling categorical columns with the most frequent value using `mode()[0]`
- Filling boolean columns with `False`
- Handling boolean columns safely by converting them to nullable boolean dtype before filling
- Filling multiple columns at once using a dictionary
- Checking missing values before and after filling
- Creating a before-and-after fillna summary DataFrame
- Applying the same missing value filling concepts to a separate customer orders dataset
- Creating a new column after filling missing values
- Saving cleaned datasets and summary results as CSV files

This practice helped me understand how to choose different missing value filling strategies depending on the meaning and data type of each column.

---

## Weekly Summary

This week focuses on missing value handling in pandas.

So far, I practiced how to:

- Create a sample dataset with missing values
- Save and read CSV files using pandas
- Check missing values using `isnull()`
- Understand that `True` means a missing value exists
- Count missing values by column
- Count total missing values in a DataFrame
- Calculate missing value percentages by column
- Filter rows that contain at least one missing value
- Count missing values by row
- Add a temporary missing value count column
- Check missing values in specific columns
- Extract complete rows with no missing values
- Check whether a DataFrame contains any missing values
- Create missing value summary DataFrames
- Filter the summary to show only columns with missing values
- Save missing value analysis results as CSV files
- Understand why `== None` should not be used to check `NaN`
- Understand that empty strings are not always treated as missing values
- Fill missing values using `fillna()`
- Fill missing categorical values with fixed values
- Fill missing numeric values with the mean
- Fill missing numeric values with the median
- Fill missing categorical values with the mode using `mode()[0]`
- Fill missing boolean values with `False`
- Handle boolean columns safely with nullable boolean dtype
- Fill different columns with different values using a dictionary
- Check missing values again after using `fillna()`
- Count total missing values after filling
- Create a before-and-after missing value summary DataFrame
- Understand that `fillna()` does not permanently modify the original DataFrame unless the result is assigned back
- Understand why using one fill value for all columns can be dangerous
- Apply `fillna()` concepts to a separate customer orders practice dataset
- Create a new column after filling missing values
- Save filled datasets and fillna summary results as CSV files

These concepts are important foundations for data cleaning, data quality checks, analysis preparation, reporting, and machine learning workflows.