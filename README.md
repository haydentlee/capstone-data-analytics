# Maricopa County Housing Affordability Analysis

Analysis of housing affordability across 126 ZIP codes in Maricopa County using Census ACS 2020-2024 data. Built two OLS regression models predicting median home value and median gross rent, visualized in a Power BI dashboard.

---

## Technologies Used

- Python
- Microsoft Power BI Desktop
- PolicyMap

---

## How to Reproduce

1. Export median household income, home value, gross rent, bachelor's degree %, and median year built at the ZCTA level from PolicyMap for Maricopa County
2. Save each as a CSV in `/datasets`
3. Run `python scripts/data_cleaning.py` then `python scripts/data_merging.py`
4. Run `python scripts/data_modeling.py` then `python scripts/regression_export.py`
5. Run `python scripts/visualizations.py`
6. Open `CIS480_Power_BI.pbix` in Power BI Desktop and reconnect data sources if prompted

---

## File Structure

```
capstone-data-analytics/
├── datasets/
├── scripts/
├── visualizations/
├── documentation/
└── CIS480_Power_BI.pbix
```

---

## Author

Hayden Lee - Mesa Community College, CIS480 Capstone
