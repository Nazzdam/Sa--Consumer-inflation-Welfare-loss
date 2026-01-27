import pandas as pd

def CompensationVaration(df, income_df):
    """
    Docstring for CompensationVaration
    
    :param df: Description
    :param income_df: Description
    calculate the compensation variation for each household
    Then find the welfare loss as a percentage of income
    """
    df=df.merge(income_df, on="Household_Id", how="left")
    df["Compensation_Variation"]=(df("Monthly_Income")*df("Household_Inflation_Rate"))
    df["Welfare loss"]=(df["Compensation_Variation"]/df["Monthly_Income"])*100
    return df