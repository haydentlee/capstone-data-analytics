import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv('maricopa_zip_merged.csv')

    # Income vs Home Value
    plt.figure()
    plt.scatter(data['median_household_income'], data['median_home_value'], color='steelblue')
    plt.xlabel('Median Household Income ($)')
    plt.ylabel('Median Home Value ($)')
    plt.title('Income vs Home Value')
    plt.savefig('income_vs_home.png')

    # Education vs Home Value
    plt.figure()
    plt.scatter(data['pct_bachelors'], data['median_home_value'], color='steelblue')
    plt.xlabel("% with Bachelor's Degree")
    plt.ylabel('Median Home Value ($)')
    plt.title("Education vs Home Value")
    plt.savefig('bachelor_vs_home.png')

    # Year Built vs Home Value
    plt.figure()
    plt.scatter(data['median_year_built'], data['median_home_value'], color='steelblue')
    plt.xlabel('Median Year Built')
    plt.ylabel('Median Home Value ($)')
    plt.title('Year Built vs Home Value')
    plt.savefig('yearbuilt_vs_home.png')

    # Income vs Rent
    plt.figure()
    plt.scatter(data['median_household_income'], data['median_gross_rent'], color='darkorange')
    plt.xlabel('Median Household Income ($)')
    plt.ylabel('Median Gross Rent ($)')
    plt.title('Income vs Rent')
    plt.savefig('income_vs_rent.png')

    # Education vs Rent
    plt.figure()
    plt.scatter(data['pct_bachelors'], data['median_gross_rent'], color='darkorange')
    plt.xlabel("% with Bachelor's Degree")
    plt.ylabel('Median Gross Rent ($)')
    plt.title("Education vs Rent")
    plt.savefig('bachelor_vs_rent.png')

    # Year Built vs Rent
    plt.figure()
    plt.scatter(data['median_year_built'], data['median_gross_rent'], color='darkorange')
    plt.xlabel('Median Year Built')
    plt.ylabel('Median Gross Rent ($)')
    plt.title('Year Built vs Rent')
    plt.savefig('yearbuilt_vs_rent.png')


  
