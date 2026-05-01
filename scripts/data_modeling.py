import pandas as pd
import statsmodels.api as sm

if __name__ == '__main__':
    data = pd.read_csv('maricopa_zip_merged.csv')
    X = sm.add_constant(data[['median_household_income','pct_bachelors','median_year_built']])

    print('=== Model 1: Median Home Value ===')
    m1 = sm.OLS(data['median_home_value'], X).fit()
    print(m1.summary())

    print('\n=== Model 2: Median Gross Rent ===')
    m2 = sm.OLS(data['median_gross_rent'], X).fit()
    print(m2.summary())

    print('\n=== Predictor correlations ===')
    print(data[['median_household_income','pct_bachelors','median_year_built']].corr().round(2))
