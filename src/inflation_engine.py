import numpy as np
import pandas

def CompHouseholdWeights(Expenditure_df):
    """
    Compute the weights of each expenditure category per household.
    """
    
    Weights=Expenditure_df.copy()
    TotalSpend=Weights.groupby("Household_Id")["Monthly_Spend"].transform("sum")
    Weights["Weight"]=Weights["Monthly_Spend"]/TotalSpend
    return Weights

def CompCatInflation(CPI_df):
    """
    Compute the monthly inflation rates per category from CPI indices.
    """
    CPI_df=CPI_df.sort_values(["Category","date"])
    CPI_df["Inflation_Rate"]=CPI_df.groupby("Category")["CPI_Index"].pct_change()
    return CPI_df.dropna()

def CompHouseholdInflation(Weights_df, Inflation_df):
    """
    Docstring for CompHouseholdInflation
    
    :param Weights_df: Description
    :param Inflation_df: Description
    
    compute the household inflation rates by merging weights with category inflation rates
    """
    Merged=Weights_df.merge(Inflation_df, on="Category", how="left")
    Merged["Weighted Inflation"]=Merged["Weight"]*Merged["Inflation_Rate"]
    HouseHoldInflation=Merged.groupby(["Household_Id","date ","income_Decile"], as_index=False)["Weighted Inflation"].sum()
    HouseHoldInflation.rename(columns={"Weighted Inflation":"Household_Inflation_Rate"}, inplace=True)
    return HouseHoldInflation