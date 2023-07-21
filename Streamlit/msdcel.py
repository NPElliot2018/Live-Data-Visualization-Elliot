import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image


#@st.cache_data

img=Image.open("E:\Elliotsystems\Streamlit\ElliotSystems.png")

st.set_page_config(
    page_title="Elliot Systems",
    page_icon=img
    )

def load_data():
    df=pd.read_csv("E:\Elliotsystems\Streamlit\MSEDCLCombine.csv",index_col="DateTime")

    numeric_df=df.select_dtypes(['float','int'])
    numeric_cols=numeric_df.columns

    text_df=df.select_dtypes(['object'])
    text_cols=text_df.columns

    Date_column=df['Date']
    unique_date=Date_column.unique()
    
    return df, numeric_cols, text_cols, unique_date
    
df, numeric_cols, text_cols, unique_date= load_data()

st.title("MSECDL Dashboard")
st.sidebar.title("Settings")

check_box=st.sidebar.checkbox(label="Display dataset")

if check_box:
    st.write(df)

st.sidebar.subheader("Timeseries settings")

feature_selection=st.sidebar.multiselect(label="Features to plot",options=numeric_cols)
date_dropdown=st.sidebar.selectbox(label="Date selector",options=unique_date)


df=df[df['Date']==date_dropdown]
df_features=df[feature_selection]


plotly_figure = px.line(data_frame=df_features,x=df_features.index, y=feature_selection, title=(str(date_dropdown) + ' ' + 'Timeline' ))

st.plotly_chart(plotly_figure)

