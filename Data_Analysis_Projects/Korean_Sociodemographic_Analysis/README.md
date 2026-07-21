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

The project follows a complete data analysis workflow, beginning with exploratory data analysis, continuing through statistical hypothesis testing, and eventually expanding into predictive modeling using machine learning.

---

# 🚀 Project Workflow

| Step | Notebook | Description | Status |
|---|---|---|---|
| 01 | `01_EDA.ipynb` | Exploratory data analysis, preprocessing, visualization, and initial findings | ✅ Completed |
| 02 | `02_Statistical_Analysis.ipynb` | Statistical hypothesis testing using Welch's t-tests with interpretation and conclusions | 🚧 In Progress |
| 03 | `03_Predictive_Model.ipynb` | Predictive modeling using machine learning algorithms | 🚧 Planned |

---

# 📊 Current Analysis

## 01. Exploratory Data Analysis (EDA)

Topics covered:

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

## 02. Statistical Analysis

Current analyses include:

- Welch's t-test for gender income differences
- Welch's t-test for divorce rates by religion
- Research question formulation
- Statistical hypothesis testing
- Hypothesis development
- Result interpretation
- Analytical conclusions

---

# 📈 Current Findings

The project currently includes two statistical hypothesis tests using Welch's t-test.

### Gender Income Gap

- Compared mean income between male and female respondents
- Tested statistical significance using Welch's t-test
- Interpreted results based on p-values and hypothesis testing

### Divorce Rates by Religion

- Compared divorce rates between respondents with and without religion
- Encoded marital status as a binary variable
- Applied Welch's t-test to compare divorce rates
- Interpreted findings with statistical conclusions

Each statistical analysis follows a structured analytical workflow:

- Research Question
- Why Statistical Testing?
- Why Welch's t-test?
- Hypotheses
- Statistical Analysis
- Results
- Interpretation
- Conclusion

---

# 📂 Data Files

| File | Included | Description |
|---|---|---|
| `Koweps_Codebook_2019.xlsx` | ✅ Yes | Codebook for coded variables |
| [`Koweps_hpwc14_2019_beta2.sav`](https://bit.ly/Koweps_hpwc14_2019_beta2) | ❌ No | Korean Welfare Panel Study dataset (excluded because of GitHub file size limitations) |

The raw survey dataset (`Koweps_hpwc14_2019_beta2.sav`) is not included in this repository because it exceeds GitHub's file size limit.

If you would like to reproduce the analysis, download the dataset from the link above and place it inside:

```text
Korean_Sociodemographic_Analysis/
└── data/
    └── Koweps_hpwc14_2019_beta2.sav
```

Once the dataset is placed in the `data/` folder, all notebooks can be executed without modification.

---

# 🛠 Technologies

## Programming Language

- Python

## Libraries

Current

- pandas
- NumPy
- matplotlib
- seaborn
- SciPy

Planned

- statsmodels
- scikit-learn

---

# 📚 Skills Demonstrated

Current

- Data loading
- Data cleaning
- Data preprocessing
- Feature engineering
- Exploratory data analysis (EDA)
- Data visualization
- Statistical hypothesis testing
- Welch's t-test
- Statistical interpretation
- Data interpretation

Planned

- Correlation analysis
- ANOVA
- Chi-square test
- Regression analysis
- Machine learning
- Model evaluation

---

# 📝 Future Improvements

- Add correlation analysis
- Perform ANOVA
- Apply Chi-square tests
- Build predictive models
- Improve visualizations
- Compare multiple machine learning algorithms
- Add feature importance analysis
- Create a final project report

---

# 📌 Notes

This project is continuously updated as new statistical and machine learning techniques are learned.

At the current stage, the statistical analysis notebook focuses on learning hypothesis testing using Welch's t-test. As additional statistical methods are learned, more appropriate techniques such as Chi-square tests, correlation analysis, ANOVA, regression analysis, and predictive modeling will be incorporated into the project.

The goal is to build a portfolio-quality project that demonstrates not only technical implementation but also analytical thinking, statistical reasoning, and clear communication of insights.