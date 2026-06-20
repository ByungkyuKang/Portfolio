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

These concepts are important foundations for data cleaning, data quality checks, analysis preparation, and machine learning workflows.