"""
This is a synthetic dataset will be used in the src modules
"""

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
        "Communivcation":0.03,
        "Other":0.02+0.05*(row["Income_Decile"]-1)
    }

Total=sum(BaseWeights.values())
Weights = {k: v / Total for k, v in BaseWeights.items()}

for Categories, Weights in Weights.items:
    records.append({
        "Hosuehold_Id":row["Household_Id"],
        "Income_Decile":row["Income_Decile"],
        "Category":Categories,
        "Monthly_Income":row["Monthly_Income"]*Weights
    })
    
#Create the Household CSV
Household_Expenditure=pd.DataFrame(records)
Household_Expenditure.to_csv("data/raw/sa_household_expenditure.csv", index=False)
Households[["Household_Id", "Monthly_Income"]].to_csv(
    "data/raw/sa_household_income.csv", index=False
)