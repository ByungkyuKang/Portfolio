# Week 03 — Functions and Files

## Overview

This week focuses on understanding Python functions and basic file handling.

The goal is to learn how to organize code into reusable functions and understand how to save simple output to text files.

Functions are important because they help reduce repeated code, improve readability, and make programs easier to test and reuse.

---

## Day 01 — Functions, Input, and Output

### Topics Covered

- Defining functions with `def`
- Function parameters and arguments
- The `return` statement
- Difference between `print()` and `return`
- Functions with one input
- Functions with multiple inputs
- Default parameters
- Using `input()` for user input
- Converting input values with `int()`
- Creating simple reusable programs with functions

### Practice File

| File | Description |
|---|---|
| [Day_01_Functions_Input_Output.ipynb](./Day_01_Functions_Input_Output.ipynb) | Practice notebook for Python functions, parameters, arguments, return values, user input, and output |

---

## Day 02 — Return and Multiple Functions

### Topics Covered

- Understanding the `return` statement
- Difference between `print()` and `return`
- Functions without `return`
- Multiple return statements
- Returning calculated values
- Returning multiple values
- Creating multiple functions
- Calling one function from another function
- Building small programs with reusable functions

### Practice File

| File | Description |
|---|---|
| [Day_02_Return_and_Multiple_Functions.ipynb](./Day_02_Return_and_Multiple_Functions.ipynb) | Practice notebook for understanding return values, creating multiple functions, and combining functions into small reusable programs |

---

## Day 03 — File Write with open() and write()

### Topics Covered

- Opening files with `open()`
- Writing text files with `write()`
- Using `with open()` for safe file handling
- Writing simple messages to text files
- Writing multiple lines with newline characters `\n`
- Using write mode `"w"`
- Using append mode `"a"`
- Using read mode `"r"` to check saved file content
- Creating folders with `os.makedirs()`
- Using `exist_ok=True` to avoid folder creation errors
- Writing variables, lists, calculation results, and formatted messages to text files
- Combining functions with file writing
- Saving simple model result messages to a text file

### Practice File

| File | Description |
|---|---|
| [Day_03_File_Write_Open.ipynb](./Day_03_File_Write_Open.ipynb) | Practice notebook for saving Python output into text files using `open()`, `write()`, and `with open()` |

### Generated Files

| Folder | Description |
|---|---|
| [../assets/Day03/](../assets/Day03/) | Contains text files generated from Day 03 file writing practice |

### Generated Text Files

| File | Description |
|---|---|
| `Day_03_first_output.txt` | Basic file writing and append mode practice |
| `day03_output_message.txt` | Simple message writing practice |
| `day03_multiple_lines.txt` | Multiple-line writing practice |
| `day03_profile.txt` | Variable value writing practice |
| `day03_skills.txt` | List item writing practice |
| `day03_number_summary.txt` | Number summary writing practice |
| `day03_even_odd_results.txt` | Even/odd result writing practice |
| `day03_learning_log.txt` | Append mode learning log practice |
| `day03_summary_message.txt` | Function-generated summary message practice |
| `day03_model_results.txt` | Model result message writing practice |

---

## Day 04 — File Read with open()

### Topics Covered

- Opening files in read mode `"r"`
- Reading text files with `read()`
- Reading one line at a time with `readline()`
- Reading all lines into a list with `readlines()`
- Reading files line by line with a `for` loop
- Using `with open()` for safe file handling
- Using `encoding="utf-8"`
- Checking file paths with `os.getcwd()` and `os.listdir()`
- Checking whether a file exists with `os.path.exists()`
- Cleaning lines with `strip()`
- Counting lines in a file
- Converting text values into numbers after reading

### Practice File

| File | Description |
|---|---|
| [Day_04_File_Read_Open.ipynb](./Day_04_File_Read_Open.ipynb) | Practice notebook for reading text files using `open()`, `read()`, `readline()`, `readlines()`, and line-by-line file processing |

### Related Files

| Folder | Description |
|---|---|
| [../assets/Day03/](../assets/Day03/) | Contains text files generated from Day 03 file writing practice and used for Day 04 file reading practice |

---

## Weekend — Memo Save Program

### Topics Covered

- Creating a simple memo saving program
- Using `input()` to receive a memo title and memo content
- Defining a function to save memo content
- Creating folders with `os.makedirs()`
- Using `exist_ok=True` to avoid folder creation errors
- Checking whether a file exists with `os.path.exists()`
- Using write mode `"w"` to create a new text file
- Using append mode `"a"` to add new memo entries to an existing file
- Writing formatted memo content to a `.txt` file
- Organizing generated text files inside the `assets/Weekend` folder

### Practice File

| File | Description |
|---|---|
| [Weekend_Memo_Save_Program.ipynb](./Weekend_Memo_Save_Program.ipynb) | Weekend practice notebook for creating a simple memo saving program using functions, user input, folder creation, and text file writing |

### Generated File

| File | Description |
|---|---|
| [memo.txt](../assets/Weekend/memo.txt) | Text file generated by the memo saving program. It stores memo titles and memo contents entered by the user. |

### Program Summary

This weekend practice focuses on creating a simple memo saving program using Python.

The program receives a memo title and memo content from the user.  
It then saves the memo into a text file inside the `assets/Weekend` folder.

If the memo file does not exist, the program creates a new file using write mode `"w"`.  
If the memo file already exists, the program uses append mode `"a"` to add the new memo without deleting the previous content.

This practice helped reinforce functions, user input, file path handling, folder creation, file existence checks, and writing text data to a `.txt` file.

---

## Weekly Summary

This week focuses on Python functions and file handling.

So far, I practiced how to:

- Define reusable functions using `def`
- Pass values into functions using parameters and arguments
- Return values from functions using the `return` statement
- Understand the difference between `print()` and `return`
- Create functions with one input
- Create functions with multiple inputs
- Use default parameter values
- Use `input()` to receive user input
- Convert user input into numeric types using `int()` and `float()`
- Build simple reusable programs using functions
- Understand that functions without `return` return `None`
- Use multiple return statements with conditional logic
- Return multiple values from a function
- Create multiple functions for separate responsibilities
- Call one function from another function
- Combine small functions to build a simple function-based program
- Open text files using `open()`
- Write text files using `write()`
- Use `with open()` to safely handle files
- Use write mode `"w"` to create or overwrite text files
- Use append mode `"a"` to add content to existing files
- Use read mode `"r"` to read saved text files
- Read entire files using `read()`
- Read one line at a time using `readline()`
- Read all lines into a list using `readlines()`
- Read files line by line using a `for` loop
- Check file paths and file existence before reading
- Clean file content using `strip()`
- Convert text values into numeric values after reading files
- Create a simple memo saving program
- Use user input to collect memo titles and memo contents
- Save memo entries into a `.txt` file
- Use file existence checks to decide between write mode and append mode
- Organize generated memo files inside the `assets/Weekend` folder

These concepts are important foundations for writing clean, reusable, and organized Python code.

They also help Python programs save results, logs, summaries, reports, memos, and processed output into files and read them back for further processing.