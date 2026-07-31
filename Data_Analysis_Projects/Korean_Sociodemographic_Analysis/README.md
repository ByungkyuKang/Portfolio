# 🇰🇷 Korean Sociodemographic Analysis

An end-to-end data analysis project using Korean Welfare Panel Study (KOWEPS) survey data.

This project explores demographic and socioeconomic patterns through exploratory data analysis (EDA), statistical analysis, and predictive modeling using Python.

Rather than presenting only statistical results, the project emphasizes hypothesis-driven analysis, interpretation of findings, and clear communication of insights through structured analytical workflows.

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

# 🔄 Analysis Workflow

```text
Raw Data
    ↓
Data Cleaning & Preprocessing
    ↓
Exploratory Data Analysis (EDA)
    ↓
Research Question
    ↓
Hypothesis Development
    ↓
Statistical Analysis
    ↓
Interpretation
    ↓
Conclusion
```

---

# 🚀 Project Workflow

| Step | Notebook | Description | Status |
|---|---|---|---|
| 01 | `01_EDA.ipynb` | Exploratory data analysis, preprocessing, visualization, and initial findings | ✅ Completed |
| 02 | `02_Statistical_Analysis.ipynb` | Statistical hypothesis testing using Welch's t-tests and Pearson correlation analysis with interpretation and conclusions | ✅ Completed |
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
- Pearson correlation analysis between age and income
- Pearson correlation analysis for respondents younger than 50 years old
- Pearson correlation analysis for respondents aged 50 years and older
- Scatter plot visualization with subgroup analysis
- Research question formulation
- Statistical hypothesis testing
- Hypothesis development
- Result interpretation
- Analytical conclusions

---

# 📈 Current Findings

The project currently includes statistical hypothesis testing using Welch's t-test and Pearson correlation analysis.

## 🔍 Key Insights

- Male respondents earned significantly higher incomes than female respondents.
- Respondents with a religion had a significantly lower divorce rate than those without a religion.
- Across all respondents, age showed a weak negative correlation with income.
- Among respondents younger than 50 years old, income showed a weak-to-moderate positive correlation with age.
- Among respondents aged 50 years and older, income showed a moderate negative correlation with age.

---

### Gender Income Gap

- Compared mean income between male and female respondents
- Tested statistical significance using Welch's t-test
- Interpreted results based on p-values and hypothesis testing

### Divorce Rates by Religion

- Compared divorce rates between respondents with and without religion
- Encoded marital status as a binary variable
- Applied Welch's t-test to compare divorce rates
- Interpreted findings with statistical conclusions

### Correlation Between Age and Income

- Examined the relationship between age and income using Pearson's correlation coefficient
- Visualized the relationship using scatter plots
- Found a weak negative correlation across all respondents

### Age-Specific Correlation Analysis

To better understand the overall relationship, the data were divided into two age groups.

#### Respondents Younger Than 50 Years Old

- Weak-to-moderate positive correlation between age and income
- Income generally increased with age among respondents younger than 50 years old

#### Respondents Aged 50 Years and Older

- Moderate negative correlation between age and income
- Income generally decreased with age among respondents aged 50 years and older

These analyses demonstrate that the relationship between age and income differs across age groups. While the overall correlation is weak, separating the data by age reveals two distinct patterns.

One of the most notable findings of this project is that the relationship between age and income differs substantially across age groups:

> **Income is positively correlated with age among respondents younger than 50 years old, but negatively correlated among respondents aged 50 years and older.**

Each statistical analysis follows a structured analytical workflow:

- Research Question
- Why Statistical Testing?
- Why This Statistical Method?
- Hypotheses
- Statistical Analysis
- Results
- Interpretation
- Conclusion
- Additional Observation (when applicable)

---

# 📂 Data Files

| File | Included | Description |
|---|---|---|
| `Koweps_Codebook_2019.xlsx` | ✅ Yes | Codebook for coded variables |
| [`Koweps_hpwc14_2019_beta2.sav`](https://bit.ly/Koweps_hpwc14_2019_beta2) | ❌ No | Korean Welfare Panel Study dataset (excluded because of GitHub's file size limitations) |

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
- Hypothesis-driven data analysis
- Statistical hypothesis testing
- Welch's t-test
- Pearson correlation analysis
- Scatter plot analysis
- Statistical interpretation
- Data interpretation

Planned

- ANOVA
- Chi-square test
- Regression analysis
- Machine learning
- Model evaluation

---

# 📝 Future Improvements

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

The current statistical analysis notebook is complete and includes Welch's t-tests and Pearson correlation analyses. Additional statistical methods such as ANOVA, Chi-square tests, regression analysis, and predictive modeling will be incorporated as new techniques are learned.

The goal of this project is to demonstrate not only technical implementation, but also analytical thinking, statistical reasoning, hypothesis-driven analysis, and the ability to communicate insights clearly through reproducible data analysis workflows.