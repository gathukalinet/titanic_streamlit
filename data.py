import streamlit as st
import pandas as pd

def load_data(url):
    df= pd.read_csv(url)
    return df

df = load_data('https://raw.githubusercontent.com/gathukalinet/surveydashboardlinet/refs/heads/main/Dataset/intro_bees.csv')
st.dataframe(df)

st.button('Rerun')

