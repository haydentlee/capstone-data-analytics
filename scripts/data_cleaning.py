import pandas as pd

def clean(filename):
    data = pd.read_csv(filename, skiprows=[1])
    data = data[['GeoID', data.columns[5]]]
    data.columns = ['zip', filename.split('_', 1)[1].replace('.csv','')]
    data['zip'] = data['zip'].astype(str).str.zfill(5)
    data.iloc[:, 1] = pd.to_numeric(data.iloc[:, 1], errors='coerce')
    return data

if __name__ == '__main__':
    files = [
        'median_household_income.csv',
        'median_home_value.csv',
        'median_gross_rent.csv',
        'pct_bachelors.csv',
        'median_year_built.csv'
    ]
    for f in files:
        data = clean(f)
        print(f, '->', len(data), 'rows,', data.iloc[:,1].isna().sum(), 'NaN')
