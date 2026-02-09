"""
This is a synthetic dataset will be used in the src modules
"""

import os
from pathlib import Path
import numpy as np
import pandas as pd
#Generate a random amount of households,and categories
np.random.seed(42)
NHouesholds=2000

Categories=["Food", "Housing", "Transport", "Utilities", "Education",
              "Healthcare", "Clothing", "Communication", "Other"]

#Created the households table/dataframe
Households=pd.DataFrame({
    "Household_Id":range(1,NHouesholds+1),
    "Income_Decile":np.repeat(range(1,11),NHouesholds/10),
    "Monthly_Income":np.random.lognormal(mean=0.9, sigma=0.4,size=NHouesholds)
})

#Assign base weights to each category
records=[]
for _, row in Households.iterrows():
    BaseWeights={
        "Food":0.30-0.015 * (row["Income_Decile"] - 1),
        "Housing":0.25,
        "Transport":0.15,
        "Utilities":0.10,
        "Education":0.05+0.005*(row["Income_Decile"]-1),
        "Healthcare":0.05,
        "Clothing":0.05,
        "Communication":0.03,
        "Other":0.02+0.05*(row["Income_Decile"]-1)
    }

Total=sum(BaseWeights.values())
Weights = {k: v / Total for k, v in BaseWeights.items()}

# Verify weights sum to 1 BEFORE using them
if abs(sum(Weights.values()) - 1) > 0.0001:  # Use small tolerance for float comparison
    print("Error: Weights do not sum to 1")
else:
    for Categories, Weight in Weights.items():  # Fixed .items and renamed to avoid shadowing
        records.append({
            "Household_Id": row["Household_Id"],  # Fixed typo
            "Income_Decile": row["Income_Decile"],
            "Category": Categories,
            "Monthly_Expenditure": row["Monthly_Income"] * Weight
        })

# Check if the data frame has been created correctly
if len(records) > 0:
    # Create the Household CSV
    Household_Expenditure = pd.DataFrame(records)

    # Ensure the output directory exists (use path relative to this file)
    output_dir = Path(__file__).resolve().parent / "Processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    household_path = output_dir / "household_expenditure.csv"
    households_path = output_dir / "households.csv"

    Household_Expenditure.to_csv(household_path, index=False)
    Households[["Household_Id", "Monthly_Income", "Income_Decile","Categories","Monthly_Expenditure"]].to_csv(households_path, index=False)

    print(f"Data set has been created and saved to {output_dir}")
else:
    print("Error: No records were created. Please check the weight calculations.")