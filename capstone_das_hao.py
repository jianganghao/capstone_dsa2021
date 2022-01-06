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
st.markdown('This dashboard is an example for the capstone project of DSA 2021-2022.' )
st.markdown('By: Jiangang Hao')
st.latex(r'''R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}''')


#--- read in data ---
dfo = read_data('data/data_capstone_dsa2021_2022.csv')

with st.expander('Display the data'):
    st.dataframe(dfo)

# -- sidebar to filter data --
st.sidebar.markdown('## Filter the Data')
age_low, age_high = st.sidebar.slider('Please select age range',18, 70,(18,70))
df = dfo.query('age>= @age_low and age <= @age_high')

st.markdown('## Data Visualization')
fig_hist = px.histogram(df,x='sum_score',color = 'gender',facet_row = 'home_computer')
st.plotly_chart(fig_hist,height = 900)

#--ballon --
c1,c2,c3 = st.columns(3)
clicked = st.button('Click to Celebrate!')
if clicked:
    c2.balloons()

