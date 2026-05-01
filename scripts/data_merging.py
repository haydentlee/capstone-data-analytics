import pandas as pd

def load_one(filename, new_col):
    data = pd.read_csv(filename, skiprows=[1])
    data = data[['GeoID', data.columns[5]]]
    data.columns = ['zip', new_col]
    data['zip'] = data['zip'].astype(str).str.zfill(5)
    data[new_col] = pd.to_numeric(data[new_col], errors='coerce')
    return data

if __name__ == '__main__':
    inc  = load_one('median_household_income.csv', 'median_household_income')
    home = load_one('median_home_value.csv', 'median_home_value')
    rent = load_one('median_gross_rent.csv', 'median_gross_rent')
    bach = load_one('pct_bachelors.csv', 'pct_bachelors')
    yb   = load_one('median_year_built.csv', 'median_year_built')

    data = inc.merge(home, on='zip').merge(bach, on='zip').merge(rent, on='zip').merge(yb, on='zip')
    data = data.dropna()
    data = data[data['median_home_value'] < 2000000]
    data = data.sort_values('zip').reset_index(drop=True)
    data.to_csv('maricopa_zip_merged.csv', index=False)
    print('Saved maricopa_zip_merged.csv with', len(data), 'rows')
