# 🧠 Portfolio

A collection of data analysis, machine learning, Python, data engineering, cloud, and software development projects.

This portfolio documents my continuous learning and career development journey, combining my professional software engineering experience with hands-on projects in Python, SQL, data analysis, statistics, machine learning, and cloud technologies.

---

## 📁 Repository Structure

<pre>
Portfolio/
│
├── Certifications&Badges/
│   ├── AWS/
│   ├── Databricks/
│   └── Kaggle/
│
├── Data_Analysis_Projects/
│   ├── Korean_Sociodemographic_Analysis/
│   └── ...
│
├── Machine_Learning_Projects/
│   ├── Titanic-Survival-Prediction/
│   └── ...
│
├── Personal_Projects/
│   ├── Unique_Img_Process_with_Python/
│   ├── Information_Scraper/
│   ├── Tip_Calculator/
│   └── ...
│
└── Data_AI_Learning_Journey/
    ├── assets/
    ├── Week_02_Python_Basics/
    ├── Week_03_Functions_and_Files/
    ├── Week_04_Mini_Project_01/
    ├── Week_05_Pandas_Basics/
    ├── Week_06_Data_Cleaning_and_Sorting/
    ├── Week_07_Missing_Value_Handling/
    └── ...        
</pre>

> Each major project is organized in its own directory with notebooks, data files, supporting images, results, and project-specific documentation.

> Large raw datasets are excluded when they exceed GitHub's file size limit. Download instructions are provided in the relevant project README files.

---

## 🎓 Certifications and Badges

This folder contains official certifications, course completion certificates, accreditations, and digital badges from platforms such as AWS, Databricks, and Kaggle.

These credentials reflect my ongoing development in cloud computing, Python, data analysis, and data engineering fundamentals.

### Official Certification

- AWS Certified Cloud Practitioner (CLF-C02) — AWS
- [Credly Badge](https://www.credly.com/badges/e81bc28a-f12f-4dab-9729-22f708352dba)

### Course Completions and Accreditations

- AWS Cloud Practitioner Essentials — AWS Training and Certification
- Databricks Fundamentals Accreditation — Databricks
- Pandas — Kaggle
- Python — Kaggle
- Intro to Programming — Kaggle

> Some items in this folder are course completions or foundational badges rather than professional certifications. They are included to document continuous learning progress.

---

## 📊 Data Analysis Projects

### 🇰🇷 Korean Sociodemographic Analysis

**Location:**  
[`Data_Analysis_Projects/Korean_Sociodemographic_Analysis/`](./Data_Analysis_Projects/Korean_Sociodemographic_Analysis/)

An end-to-end data analysis project using Korean Welfare Panel Study (KOWEPS) survey data.

The project investigates relationships among demographic and socioeconomic variables such as income, gender, age, occupation, religion, marital status, and region.

The project currently covers the workflow from exploratory data analysis and statistical hypothesis testing to interpretation of findings. Predictive modeling using machine learning will be added in the next phase.

The project follows a structured analytical workflow:

- Data cleaning and preprocessing
- Exploratory data analysis
- Feature creation
- Grouped summary analysis
- Data visualization
- Statistical analysis
- Interpretation of findings and limitations
- Predictive modeling (planned)

### Project Progress

| Stage | Notebook | Status |
|---|---|---|
| Exploratory Data Analysis | `01_EDA.ipynb` | ✅ Completed |
| Statistical Analysis | `02_Statistical_Analysis.ipynb` | ✅ Completed |
| Predictive Modeling | `03_Predictive_Model.ipynb` | 🚧 Planned |

[View the project README](./Data_Analysis_Projects/Korean_Sociodemographic_Analysis/README.md)

---

## 🤖 Machine Learning Projects

### 🧩 Titanic Survival Prediction

**Location:**  
[`Machine_Learning_Projects/Titanic-Survival-Prediction/`](./Machine_Learning_Projects/Titanic-Survival-Prediction/)

A foundational machine learning project using the Titanic passenger dataset.

This project covers an end-to-end introductory machine learning workflow, including data exploration, preprocessing, feature engineering, model training, cross-validation, and evaluation.

### Key Learning Areas

- Data loading and inspection
- Exploratory data analysis
- Missing value handling
- Feature engineering
- Categorical and numerical data analysis
- Data visualization
- Correlation analysis
- Logistic Regression
- Decision Tree classification
- Cross-validation
- Confusion matrix analysis
- Classification metrics
- Overfitting identification

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 score
- ROC-AUC

**Goal:** Build practical experience with the complete machine learning workflow, from raw data exploration to model evaluation and interpretation.

**Dataset:** Kaggle Titanic — Machine Learning from Disaster

---

## 📘 Data & AI Learning Journey

**Location:**  
[`Data_AI_Learning_Journey/`](./Data_AI_Learning_Journey/)

A structured learning series focused on Python, pandas, data cleaning, statistics, data analysis, and data engineering fundamentals.

This section documents step-by-step learning through notebooks, exercises, and small projects.

The techniques learned here are gradually applied to the larger portfolio projects.

### Learning Workflow

```text
Study a concept
        ↓
Practice it in a learning notebook
        ↓
Review and improve the notebook
        ↓
Apply the technique to a portfolio project
        ↓
Document findings and update the project README
```

The goal is to connect theoretical learning directly to practical portfolio development.

### Completed and In-Progress Topics

#### Week 02 — Python Basics

- Variables, numbers, and strings
- Lists and dictionaries
- Indexing
- Conditional statements
- Comparison operators
- Loops and `range()`
- Basic practice programs

#### Week 03 — Functions and Files

- Functions with parameters
- Return values
- Multiple-function program structure
- File writing with `open()`
- File reading with `read()`, `readline()`, and `readlines()`
- Simple file-based programs

#### Week 04 — Mini Project 01

**Project:** Multiplication Table TXT Saver

- User input
- Function-based program structure
- Nested loops
- File writing and reading
- Generating and saving text output
- Creating a small complete Python application

#### Week 05 — Pandas Basics

- pandas installation and import
- DataFrame creation
- Reading CSV files
- Selecting columns
- Filtering rows
- Basic CSV data analysis

#### Week 06 — Data Cleaning and Sorting

- Sorting DataFrames with `sort_values()`
- Conditional filtering
- Adding calculated columns
- Creating Boolean columns
- Using `.loc[]`
- Using `.copy()` after filtering
- Grouping with `groupby()`
- Creating grouped summaries with `agg()`
- Saving analysis results as CSV files

#### Week 07 — Missing Value Handling

- Understanding `NaN`
- Detecting missing values with `isnull()`
- Counting missing values by column and row
- Calculating missing-value percentages
- Filtering rows containing missing values
- Creating missing-value summary tables
- Filling missing values with `fillna()`
- Using mean, median, mode, and fixed values
- Comparing data before and after treatment

**Goal:** Build strong foundations in Python, pandas, data cleaning, statistics, and practical data preparation for future data analysis, data engineering, and machine learning projects.

---

## 🧰 Personal Projects

### 🖼️ Unique Image Organizer

**Location:**  
[`Personal_Projects/Unique_Img_Process_with_Python/`](./Personal_Projects/Unique_Img_Process_with_Python/)

A Python desktop utility for identifying and organizing duplicate or visually similar images.

### Key Features

- Scans directories for image files
- Detects duplicate and similar images
- Uses hash-based and feature-based image comparison
- Groups matching images
- Sorts images by resolution
- Displays images through a graphical interface
- Supports image preview
- Allows selected-image deletion
- Supports automatic cleanup while keeping the highest-resolution image
- Helps organize large personal image collections

### Tech Stack

- Python
- OpenCV
- Pillow
- ImageHash
- Tkinter
- OS and file-system modules

**Goal:** Build a practical desktop application that solves a real file-management problem while practicing modular Python development, image processing, and graphical user interface design.

---

### 🌐 Information Scraper

**Location:**  
[`Personal_Projects/Information_Scraper/`](./Personal_Projects/Information_Scraper/)

A web scraping project intended to collect, organize, and export useful information from selected websites.

### Current Status

- Initial project structure created
- Foundation script prepared for future development

### Planned Areas

- HTTP requests
- HTML parsing
- Data extraction
- Data cleaning
- Structured output generation
- Error handling

**Goal:** Learn practical web scraping, request handling, parsing, and structured data collection.

---

### 💰 Tip Calculator

**Location:**  
[`Personal_Projects/Tip_Calculator/`](./Personal_Projects/Tip_Calculator/)

A tip distribution application that divides a total tip amount among multiple participants based on hours worked.

### Key Features

- Accepts a total tip amount
- Allows names and hours to be entered
- Dynamically generates participant input rows
- Calculates the hourly tip rate
- Distributes tips based on hours worked
- Handles rounding differences
- Saves and reloads participant information
- Supports deployment as a web application
- Uses Docker for packaging and deployment

### Live Application

[Open Tip Calculator](https://starbucks-tip-out.onrender.com)

### Tech Stack

- Python
- Flet
- FastAPI
- JSON
- Docker
- Uvicorn
- Render

**Goal:** Practice interactive application development, dynamic user-interface updates, data persistence, containerization, and cloud deployment.

---

## 🚀 Current Development Goals

- Continue building portfolio-quality data analysis projects
- Apply newly learned statistical methods to existing projects
- Strengthen SQL and Python skills for data-focused roles
- Practice statistical hypothesis testing and regression analysis
- Build practical data pipelines
- Expand machine learning projects using scikit-learn
- Improve project documentation and reproducibility
- Continue AWS certification study
- Learn additional AWS data services
- Build projects combining analysis, databases, automation, and cloud technologies

---

## 🧑‍💻 About Me

I am a software engineer transitioning toward data-focused roles, including Data Analyst and Data Engineer positions.

I have more than nine years of professional experience developing and maintaining backend systems in healthcare-related production environments. My professional background includes C programming, Oracle SQL, embedded SQL and PL/SQL, Linux and UNIX systems, batch processing, data validation, automation, and production support.

I am expanding this experience through hands-on projects in Python, pandas, data analysis, statistics, machine learning, cloud computing, and data engineering.

My goal is to combine my software development background with strong analytical, database, automation, and data-processing skills to contribute effectively to data-focused teams.

---

## 🏷️ Tech Stack

### Programming Languages

- Python
- C
- SQL
- Shell scripting

### Data Analysis

- pandas
- NumPy
- Seaborn
- SciPy
- Jupyter Notebook
- Exploratory Data Analysis
- Data cleaning and preprocessing
- Data visualization

### Databases

- Oracle
- SQL
- PL/SQL
- Embedded SQL / Pro*C
- Relational database concepts

### Machine Learning

- scikit-learn
- Feature engineering
- Classification
- Cross-validation
- Model evaluation

### Software Development

- Modular programming
- Backend development
- Batch processing
- Debugging
- Production support
- Test documentation
- Code review workflows

### Applications and Deployment

- Tkinter
- Flet
- FastAPI
- Docker
- Uvicorn
- Render

### Cloud and Data Platforms

- AWS cloud fundamentals
- Databricks fundamentals

### Development Tools

- Git
- GitHub
- VS Code
- Linux
- UNIX
- Jupyter Notebook
- GitHub Copilot

### Currently Expanding

- Regression analysis
- Data engineering workflows
- AWS data services
- Advanced SQL
- Predictive modeling
- PyTorch
- MLflow
- MLOps fundamentals

---

## 📫 Contact

- **Email:** [byungkyukang702@gmail.com](mailto:byungkyukang702@gmail.com)
- **LinkedIn:** [linkedin.com/in/byungkyukang](https://www.linkedin.com/in/byungkyukang)
- **GitHub:** [github.com/ByungkyuKang](https://github.com/ByungkyuKang)