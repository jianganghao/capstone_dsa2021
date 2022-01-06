import streamlit as st
import pandas as pd
import plotly.express as px

# -- define functions -----
@st.cache
def read_data(file_path_name):
    df = pd.read_csv(file_path_name)
    return df

# -- title --
st.title("Data Safari for Capstone Project")
st.markdown('This dashboard is for the capstone project of DSA 2021-2022.' )
st.markdown('By: Jiangang Hao')

#--- read in data ---
df = read_data('data/data_capstone_dsa2021_2022.csv')

show_data = st.buttion('Click to display data')
if show_data:
    st.dataframe(df)

st.markdown('## Data Summary')
st.sidebar.markdown('## Filter the Data')
select_category = st.sidebar.selectbox('Please choose gender',['Male','Female'])
fig_hist = px.histogram(df.query('gender == @select_category'),x='sum_score',animation_frame = 'home_computer')
st.plotly_chart(fig_hist)

clicked = st.button('Click to Celebrate!')
if clicked:
    st.balloons()

