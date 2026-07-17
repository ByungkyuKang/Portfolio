# 📊 Data Analysis Projects

This folder contains data analysis projects focused on exploratory data analysis, data preprocessing, visualization, and interpretation using Python and pandas.

The goal of this folder is to practice complete data analysis workflows using real-world datasets.

---

## 📁 Folder Structure

<pre>
Data_Analysis_Projects/
├── data/
│   └── Supporting datasets and codebook files
│
├── 01. korean_sociodemographic_analysis.ipynb
└── README.md
</pre>

> The `data/` folder contains supporting datasets and codebook files used in the analysis notebooks.

> Large raw data files such as `.sav` files are not included in this repository because they may exceed GitHub's file size limit. Please place the required raw dataset manually inside the `data/` folder before running the notebook.

---

## 📌 Project List

| No. | Project | Notebook | Main Topics |
|---|---|---|---|
| 01 | Korean Sociodemographic Analysis | [Notebook](./01.%20korean_sociodemographic_analysis.ipynb) | Income, gender, age, occupation, religion, region |

---

## 01 — Korean Sociodemographic Analysis

### Project Overview

This project analyzes Korean sociodemographic data using Python and pandas.

The analysis focuses on relationships between demographic and social variables such as income, gender, age, occupation, religion, marital status, and region.

The project uses survey-style welfare data and codebook information to clean coded variables, create readable categories, summarize grouped data, and visualize important social patterns.

---

### Topics Covered

- Data loading and inspection
- SPSS data import using `read_spss()`
- Data preprocessing
- Column renaming
- Missing value handling
- Derived column creation
- Grouped summary analysis
- Codebook-based occupation mapping
- Gender wage gap analysis
- Age and income analysis
- Income analysis by age group
- Income analysis by occupation
- Job frequency comparison by gender
- Religion and divorce rate analysis
- Regional elderly population analysis
- Data visualization
- Interpretation of key findings and limitations

---

### Project File

| File | Description |
|---|---|
| [01. korean_sociodemographic_analysis.ipynb](./01.%20korean_sociodemographic_analysis.ipynb) | Exploratory data analysis notebook using Korean welfare survey data |

---

### Data Files

| File | Included in Repository | Description |
|---|---|---|
| `Koweps_Codebook_2019.xlsx` | Yes | Codebook file used to map coded variables such as occupation codes |
| [`Koweps_hpwc14_2019_beta2.sav`](https://bit.ly/Koweps_hpwc14_2019_beta2) | No | Main Korean welfare survey dataset excluded from this repository because it exceeds GitHub's file size limit |

> The main `.sav` dataset is not included in this repository because it exceeds GitHub's file size limit.
>
> To run the notebook, download `Koweps_hpwc14_2019_beta2.sav` from the link above and place it manually inside the `Data_Analysis_Projects/data/` folder.

---

### Libraries Used

- Python
- pandas
- NumPy
- seaborn
- matplotlib

---

### Project Summary

In this project, I practiced a complete exploratory data analysis workflow using Korean welfare survey data.

The project includes data loading, inspection, preprocessing, variable transformation, grouped summary analysis, visualization, and interpretation of sociodemographic patterns.

This project helped me practice how to analyze real-world survey-style data and communicate findings using pandas and visualization tools.

---

## 🧰 Skills Practiced

- Reading structured data files
- Inspecting data structure
- Cleaning and transforming coded variables
- Handling missing values
- Creating new analytical columns
- Grouping and summarizing data
- Joining codebook information with analysis data
- Creating visualizations
- Interpreting data analysis results
- Documenting project limitations

---

## 📝 Notes

This README is intended to provide a high-level overview of the data analysis projects in this folder.

As more projects are added, each project will be listed in the project table with a short summary. Detailed explanations can be documented inside each project notebook or in separate project-specific README files when needed.