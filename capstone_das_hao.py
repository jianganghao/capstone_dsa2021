import streamlit as st
import pandas as pd
import plotly.express as px

# -- title --
st.title("Data Safari for Capstone Project")
st.markdown('This dashboard is for the capstone project of DSA 2021-2022.' )
st.markdown('By: Jiangang Hao')

#--- read in data ---
df = pd.read_csv('data/data_capstone_dsa2021_2022.csv')

st.dataframe(df)

st.markdown('## Data Summary')
select_category = st.selectbox('Please choose the subset',['gender','has_home_computer'])
st.write(select_category)
fig_hist = px.histogram(df,x='sum_score')
st.plotly_chart(fig_hist)

