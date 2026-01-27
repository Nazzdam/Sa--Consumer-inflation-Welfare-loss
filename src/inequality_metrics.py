def CompInequalityMetrics(df, income_df):
    """
    This function computes various inequality metrics.
    Currently, it is a placeholder and does not implement any functionality.
    """
    df=df.merge(income_df, on="Household_Id", how="left")
    Summary=df.groupby("Income_Decile")["Welfare_loss"].mean()
    InequalityGap=Summary["Household_Inflation_Rate"].quantle(0.9)-Summary["Household_Inflation_Rate"].quantile(0.1)
    return Summary ,InequalityGap