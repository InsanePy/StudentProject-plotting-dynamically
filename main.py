import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search of Happiness")
x_option = st.selectbox("Select the data for X-axis",
                        options=("GDP", "Happiness", "Generosity"))
y_option = st.selectbox("Select the data for Y-axis",
                        options=("GDP", "Happiness", "Generosity"))
st.subheader(f"{x_option} and {y_option}")

df = pd.read_csv("happy.csv")
gdp = df["gdp"]
figure = px.scatter(x=df[str(x_option).lower()], y=df[str(y_option).lower()],
                    labels={"x": f"{x_option}", "y": f"{y_option}"})
st.plotly_chart(figure)