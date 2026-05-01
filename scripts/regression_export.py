import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

if __name__ == '__main__':
    data = pd.read_csv('maricopa_zip_merged.csv')
    data = data.dropna()
    data = data[data['median_home_value'] < 2000000]
    print('n =', len(data))

    predictors = ['median_household_income', 'pct_bachelors', 'median_year_built']
    X = sm.add_constant(data[predictors])

    models = {
        'Median Home Value': data['median_home_value'],
        'Median Gross Rent': data['median_gross_rent']
    }

    coef_rows = []
    fit_rows = []

    for label, y in models.items():
        m = sm.OLS(y, X).fit()
        print(f'\n=== {label} ===')
        print(m.summary())

        sd_y = y.std()
        for p in predictors:
            sd_x = data[p].std()
            beta = m.params[p]
            se = m.bse[p]
            t = m.tvalues[p]
            pval = m.pvalues[p]
            ci_low, ci_high = m.conf_int().loc[p]
            std_beta = beta * sd_x / sd_y
            coef_rows.append({
                'model': label,
                'predictor': p,
                'beta': round(beta, 4),
                'std_beta': round(std_beta, 4),
                'se': round(se, 4),
                't_stat': round(t, 3),
                'p_value': round(pval, 4),
                'ci_low': round(ci_low, 4),
                'ci_high': round(ci_high, 4),
                'significant': 'Yes' if pval < 0.05 else 'No'
            })

        fit_rows.append({
            'model': label,
            'n': int(m.nobs),
            'r_squared': round(m.rsquared, 4),
            'adj_r_squared': round(m.rsquared_adj, 4),
            'f_statistic': round(m.fvalue, 2),
            'f_p_value': round(m.f_pvalue, 6),
            'df_model': int(m.df_model),
            'df_resid': int(m.df_resid)
        })

    vif_rows = []
    for i, col in enumerate(X.columns):
        if col == 'const':
            continue
        vif_rows.append({
            'predictor': col,
            'vif': round(variance_inflation_factor(X.values, i), 3)
        })

    pd.DataFrame(coef_rows).to_csv('regression_coefficients.csv', index=False)
    pd.DataFrame(fit_rows).to_csv('regression_fit_stats.csv', index=False)
    pd.DataFrame(vif_rows).to_csv('regression_vif.csv', index=False)

    print('\nSaved: regression_coefficients.csv, regression_fit_stats.csv, regression_vif.csv')
