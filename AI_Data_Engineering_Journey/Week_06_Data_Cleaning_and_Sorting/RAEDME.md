# Week 06 — Data Cleaning and Sorting

## Overview

This week focuses on basic data cleaning, filtering, and sorting using pandas.

The goal is to organize DataFrames more effectively by sorting values, filtering rows, and preparing data for simple analysis workflows.

---

## Day 01 — Sorting Data with sort_values()

### Topics Covered

- Understanding what `sort_values()` does
- Sorting DataFrames by one column
- Sorting numeric columns in ascending order
- Sorting numeric columns in descending order
- Sorting text columns alphabetically
- Sorting by multiple columns
- Using different sorting directions with `ascending`
- Understanding that `sort_values()` returns a new DataFrame by default
- Resetting index after sorting with `reset_index(drop=True)`
- Saving sorted DataFrames as CSV files

### Practice File

| File | Description |
|---|---|
| [Day_01_Sort_Values.ipynb](./Day_01_Sort_Values.ipynb) | Practice notebook for sorting pandas DataFrames using `sort_values()` |

### Input File

| File | Description |
|---|---|
| [students.csv](../assets/Week06/Day01/Input/students.csv) | Sample student dataset used for sorting practice |

### Output Files

| File | Description |
|---|---|
| [students_sorted_by_score.csv](../assets/Week06/Day01/Output/students_sorted_by_score.csv) | CSV file containing students sorted by score in descending order |
| [top_students.csv](../assets/Week06/Day01/Output/top_students.csv) | CSV file containing the top 3 students based on score |

---

## Day 02 — Conditional Filtering in pandas

### Topics Covered

- Understanding conditional filtering in pandas
- Creating a sample employee performance dataset
- Saving a DataFrame as a CSV file using `to_csv()`
- Reading a CSV file using `pd.read_csv()`
- Creating boolean conditions from DataFrame columns
- Storing filtering conditions in variables
- Filtering rows with numeric conditions
- Filtering rows with string conditions
- Filtering rows with boolean columns
- Filtering rows with multiple conditions using `&`
- Filtering rows with OR conditions using `|`
- Filtering rows with `isin()`
- Filtering rows with `between()`
- Filtering rows and selecting columns together using `.loc[]`
- Saving filtered DataFrames as CSV files

### Practice File

| File | Description |
|---|---|
| [Day_02_Conditional_Filtering.ipynb](./Day_02_Conditional_Filtering.ipynb) | Practice notebook for filtering pandas DataFrames using conditions, boolean columns, multiple conditions, `isin()`, `between()`, and `.loc[]` |

### Input File

| File | Description |
|---|---|
| [employee_performance.csv](../assets/Week06/Day02/Input/employee_performance.csv) | Sample employee performance dataset used for conditional filtering practice |

### Output Files

| File | Description |
|---|---|
| [high_performers.csv](../assets/Week06/Day02/Output/high_performers.csv) | CSV file containing employees with high performance scores |
| [engineering_high_scores.csv](../assets/Week06/Day02/Output/engineering_high_scores.csv) | CSV file containing Engineering employees with high scores |

---

## Weekly Summary

This week focuses on basic data cleaning, filtering, and sorting using pandas.

So far, I practiced how to:

- Sort DataFrames using `sort_values()`
- Sort data in ascending and descending order
- Sort by numeric columns
- Sort by text columns
- Sort by multiple columns
- Reset the index after sorting
- Save sorted results as CSV files
- Create boolean conditions from DataFrame columns
- Store filtering conditions in variables
- Filter rows using numeric, string, and boolean conditions
- Combine multiple filtering conditions using `&`
- Use OR filtering conditions using `|`
- Use `isin()` to filter rows by multiple possible values
- Use `between()` to filter rows within a numeric range
- Use `.loc[]` to filter rows and select columns at the same time
- Save filtered results as CSV files

These concepts are important foundations for organizing, filtering, and preparing structured data for analysis, reporting, and machine learning workflows.