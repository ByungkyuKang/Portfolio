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

These concepts are important foundations for organizing and preparing structured data for analysis, reporting, and machine learning workflows.