"""
Create a Streamlit app that displays the inflation, inequality and welfare loss metrics.
"""
import streamlit as st
import pandas as pd
from src.inflation_engine import CompHouseholdWeights, CompCatInflation, CompHouseholdInflation
from src.welfare_calculator import CompensationVaration
from src.inequality_metrics import CompInequalityMetrics

st.set_page_config(page_title="SA Inflation and Welfare Dashboard", layout="wide")
st.title("🇿🇦 Consumer Inflation & Welfare Loss Calculator")
# Load data

@st.cache_data
def load_data():
    Exp=pd.read_csv("data/Expenditure_Data.csv")
    Cpi=pd.read_csv("data/CPI_Data.csv", parse_dates=["date"])
    Income=pd.read_csv("data/Income_Data.csv")
    return Exp, Cpi, Income

Exp, Cpi, Income= load_data()

# Compute metrics
Weights=CompHouseholdWeights(Exp)
Inflation=CompCatInflation(Cpi, Weights)
HHInflation=CompHouseholdInflation(Exp, Inflation, Weights)
WelfareLoss=CompensationVaration(HHInflation, Exp, Weights)
Summary, InequalityGap=CompInequalityMetrics(WelfareLoss, Income)

tab1, tab2, tab3, tab4=st.tabs([
    "📊 Overview",
    "👪 Household Impact",
    "🛒 Category Exposure",
    "🧪 Policy Simulator"
])

with tab1:
    st.subheader("Inflation by Income Decile")
    st.bar_chart(Summary.set_index("Income_Decile"))
    st.metric("infaltion Inequality Gap (90th - 10th Percentile)", f"{InequalityGap:.2f}%")
    
with tab2:
    st.subheader("Welfare loss Distribution")
    st.dataframe(WelfareLoss.sample(100))
    st.line_chart(WelfareLoss.groupby("Income_Decile")["Welfare_loss"].mean())
    
with tab3:
    st.subheader("Category Inflation Exposure")
    st.line_chart(Inflation.pivot(index="date",columns="Category", values="Inflation_rate",))
    
with tab4:
    st.subheader("Policy shock Simulator")
    shock=st.slider("inflation Shock (%)",min_value= -0.5, max_value=0.006, value=0.0, step=0.001)
    WelfareLoss["Shock Adjusted_Inflation"] = WelfareLoss["Household_Inflation_Rate"] + shock/100
    WelfareLoss["Shock_CV"]=WelfareLoss["monthly_Income"] * WelfareLoss["Shock Adjusted_Inflation"]
    st.metric("Average Welfare Loss with Shock", f"{WelfareLoss['Shock_CV'].mean():.2f}")