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

---

## Day 03 — Add New Columns in pandas

### Topics Covered

- Understanding how to add new columns to a pandas DataFrame
- Creating a sample employee performance dataset
- Adding a column with a fixed value
- Creating calculated columns from existing numeric columns
- Creating a percentage-based column from a score column
- Converting years of experience into months
- Creating boolean columns based on conditions
- Filtering rows using a newly created boolean column
- Creating conditional columns using `.loc[]`
- Creating score level categories based on numeric conditions
- Combining multiple conditions with `&`
- Creating a bonus eligibility column
- Creating text-based label columns by combining existing string columns
- Using `.copy()` before adding columns to filtered DataFrames
- Saving DataFrames with newly added columns as CSV files

### Practice File

| File | Description |
|---|---|
| [Day_03_Add_New_Columns.ipynb](./Day_03_Add_New_Columns.ipynb) | Practice notebook for adding fixed, calculated, boolean, conditional, and text-based columns to pandas DataFrames |

### Input File

| File | Description |
|---|---|
| [employee_performance.csv](../assets/Week06/Day03/Input/employee_performance.csv) | Sample employee performance dataset used for adding new columns practice |

### Output Files

| File | Description |
|---|---|
| [employee_with_new_columns.csv](../assets/Week06/Day03/Output/employee_with_new_columns.csv) | CSV file containing the full employee dataset with newly added columns |
| [high_score_bonus_employees.csv](../assets/Week06/Day03/Output/high_score_bonus_employees.csv) | CSV file containing employees who are eligible for a bonus based on score and active status |

### Practice Summary

In this notebook, I practiced adding new columns to a pandas DataFrame.

The practice includes:

- Adding a fixed value column
- Creating calculated columns
- Creating a boolean column
- Creating a conditional score level column
- Creating a bonus eligibility column using multiple conditions
- Creating a text label column
- Adding a new column after filtering with `.copy()`

This practice helped me understand how pandas can be used to transform and enrich tabular data.

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
- Add new columns with fixed values
- Create calculated columns from existing numeric columns
- Create boolean columns based on conditions
- Create conditional columns using `.loc[]`
- Create category-style columns such as score levels
- Create text-based label columns by combining existing columns
- Use `.copy()` before adding columns to filtered DataFrames
- Save DataFrames with newly added columns as CSV files

These concepts are important foundations for organizing, filtering, transforming, and preparing structured data for analysis, reporting, and machine learning workflows.