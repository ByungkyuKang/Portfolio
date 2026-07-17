# 🇰🇷 Korean Sociodemographic Analysis

An end-to-end data analysis project using Korean Welfare Panel Study (KOWEPS) survey data.

This project explores demographic and socioeconomic patterns through exploratory data analysis (EDA), statistical analysis, and predictive modeling using Python.

---

# 📁 Project Structure

<pre>
Korean_Sociodemographic_Analysis/
├── README.md
├── data/
├── images/
├── results/
├── 01_EDA.ipynb
├── 02_Statistical_Analysis.ipynb
└── 03_Predictive_Model.ipynb
</pre>

> The `data/` folder contains supporting datasets and codebook files required for the analysis.

> Large raw datasets are not included in this repository because they exceed GitHub's file size limit. Please download them separately and place them inside the `data/` folder before running the notebooks.

---

# 📌 Project Overview

The Korean Welfare Panel Study (KOWEPS) provides nationwide survey data covering various demographic and socioeconomic characteristics.

Using this dataset, this project investigates relationships among variables such as:

- Income
- Gender
- Age
- Occupation
- Education
- Religion
- Marital status
- Region

The project is designed as a complete data analysis workflow rather than a single notebook. As additional statistical and machine learning techniques are learned, the project will continue to expand.

---

# 🚀 Project Workflow

| Step | Notebook | Description | Status |
|---|---|---|---|
| 01 | `01_EDA.ipynb` | Exploratory data analysis, preprocessing, visualization, and initial findings | ✅ Completed |
| 02 | `02_Statistical_Analysis.ipynb` | Statistical analysis including hypothesis testing, correlation analysis, and ANOVA | 🚧 Planned |
| 03 | `03_Predictive_Model.ipynb` | Predictive modeling using machine learning algorithms | 🚧 Planned |

---

# 📊 Current Analysis (01_EDA)

### Topics Covered

- Data loading and inspection
- SPSS data import using `read_spss()`
- Data preprocessing
- Variable renaming
- Missing value handling
- Feature engineering
- Grouped summary analysis
- Occupation code mapping using codebook
- Income analysis by gender
- Income analysis by age
- Income analysis by occupation
- Occupation frequency by gender
- Religion and divorce analysis
- Regional elderly population analysis
- Data visualization
- Interpretation of findings

---

# 📂 Data Files

| File | Included | Description |
|---|---|---|
| `Koweps_Codebook_2019.xlsx` | ✅ Yes | Codebook for coded variables |
| [`Koweps_hpwc14_2019_beta2.sav`](https://bit.ly/Koweps_hpwc14_2019_beta2) | ❌ No | Korean Welfare Panel Study dataset (excluded because of GitHub file size limitations) |

The raw survey dataset (`Koweps_hpwc14_2019_beta2.sav`) is not included in this repository because it exceeds GitHub's file size limit.

If you would like to reproduce the analysis, you can download the dataset from the link above and place it inside the project's `data/` folder:

```text
Korean_Sociodemographic_Analysis/
└── data/
    └── Koweps_hpwc14_2019_beta2.sav
```

Once the dataset is placed in the `data/` folder, the notebooks can be executed without any additional modifications.

---

# 🛠 Technologies

### Programming Language

- Python

### Libraries

- pandas
- NumPy
- matplotlib
- seaborn

Future notebooks will additionally use:

- SciPy
- statsmodels
- scikit-learn

---

# 📈 Project Goals

This project aims to demonstrate the complete lifecycle of a real-world data analysis project.

The final project will include:

- Exploratory Data Analysis (EDA)
- Statistical hypothesis testing
- Correlation analysis
- Regression analysis
- Predictive modeling
- Model evaluation
- Result interpretation
- Business insights

---

# 📚 Skills Demonstrated

Current

- Data loading
- Data cleaning
- Data preprocessing
- Feature engineering
- Exploratory data analysis
- Data visualization
- Data interpretation

Planned

- Statistical inference
- Hypothesis testing
- Correlation analysis
- Regression
- Machine learning
- Model evaluation

---

# 📝 Future Improvements

- Add statistical hypothesis testing
- Perform correlation analysis
- Build predictive models
- Improve visualizations
- Compare multiple machine learning algorithms
- Add feature importance analysis
- Create a final project report

---

# 📌 Notes

This project is continuously updated as new statistical and machine learning techniques are learned.

The goal is to build a portfolio-quality project that demonstrates not only technical implementation but also analytical thinking, statistical reasoning, and clear communication of insights.