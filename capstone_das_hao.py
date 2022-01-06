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
select_category = st.selectbox('Please choose gender',['Male','Female'])
st.write(select_category)
fig_hist = px.histogram(df.query('gender == @select_category'),x='sum_score',animation_frame = 'home_computer')
st.plotly_chart(fig_hist)

