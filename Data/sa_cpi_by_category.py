import numpy as np
import pandas as pd

#GENERATED A random seed

np.random.seed(42)
Categories=["Food", "Housing", "Transport", "Utilities", "Education",
              "Healthcare", "Clothing", "Communication", "Other"]
dates = pd.date_range(start="2015-01-01", end="2025-12-01", freq="MS")

#Created inflationary trends 
InflationTrend={
    "Food": 6.5,
    "Housing": 5.0,
    "Transport": 7.0,
    "Utilities": 8.0,
    "Education": 6.0,
    "Healthcare": 5.5,
    "Clothing": 4.0,
    "Communication": 3.5,
    "Other": 4.5
}

records=[]
for category in Categories:
    index=100
    for date in dates:
        InflationShock=np.random.normal(0, 0.80)
        index *= (1 + (InflationTrend[category] + InflationShock / 1200))
        records.append({"date": date, "category": category, "cpi_index": index})

cpi = pd.DataFrame(records)
cpi.to_csv("data/raw/sa_cpi_by_category.csv", index=False)        