# Exploratory Data Analysis (EDA): Housing Market Trends

##  Project Overview
This repository contains a comprehensive Exploratory Data Analysis (EDA) framework built using Python. Using a simulated residential real estate dataset, this project investigates patterns, reveals data anomalies, assesses core numerical correlations, and produces structured visual assets to guide downstream statistical workflows or machine learning feature selections.

##  Key Insights & Analysis Steps
1.  **Data Profiling:** Assessed missing data thresholds, column data types, and shape configurations.
2.  **Descriptive Statistics:** Extracted statistical dispersion characteristics (mean, median, standard deviation, percentiles).
3.  **Univariate Analysis:** Inspected the underlying distribution and skewness of the target metric (`Price_USD`).
4.  **Bivariate/Multivariate Investigation:** Evaluated how living area dimensions (`Square_Feet`) and localized categorical indicators (`Neighborhood`) scale relative to asset valuation.
5.  **Multivariate Feature Interaction:** Plotted structural matrices to evaluate cross-feature correlation intensities.

##  Stack Components
* **Pandas & NumPy:** Core data transformation, subsetting, and tabular aggregations.
* **Matplotlib & Seaborn:** Programmatic charting, density curve modeling, and linear regression fitting.

## Visual Discoveries
All visualizations are systematically exported to the `/eda_plots` folder:
* `1_price_distribution.png`: Histogram identifying target distribution skewness.
* `2_price_vs_sqft.png`: Linear regression tracking variance between square footage and market valuation.
* `3_price_by_neighborhood.png`: Side-by-side boxplots parsing variance structures across geographical regions.
* `4_correlation_matrix.png`: Heatmap exposing linear strength metrics between numerical vectors.

##  Usage Instruction
```bash
# Clone this project repository
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO.git](https://github.com/YOUR_USERNAME/YOUR_REPO.git)

# Install requirements
pip install pandas numpy matplotlib seaborn

# Execute analysis script
python eda_project.py

B
