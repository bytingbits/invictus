import streamlit as st
import pandas as pd
import plotly.graph_objects as go 
import calendar
from datetime import datetime 
import pickle
#from pathlib import Path

import streamlit_authenticator as stauth

#homepage settings
page_title ="invictus"
page_icon = ":shield:"
layout = "wide"
records= ":memo:"

st.set_page_config(page_title=page_title, layout=layout, page_icon=page_icon)
#st.sidebar.success("Select a page: ")#to nav bn pages
st.title(page_icon + " " + page_title + " " + page_icon + " ")

#---selecting time period---
years = [datetime.today().year]
months = list(calendar.month_name[1:])

st.header("what is invictus?")
"Invictus is a web app to help gender minorities with chronic pain.\n\n"
"80% of studies conducted use male subjects. This has led to a huge bias and under-diagnosis of patients of other genders."
"\nMenstrual cycles can impact chronic pain significantly due to hormonal fluctuations. Invictus takes this into account before generating insights."


#st.header(records+ " health record history ")
#with st.form("entry_form", clear_on_submit=True): 
    #col1, col2 = st.columns(2); 
    #col1.selectbox("Month: ", months, key="month") #key arg: to retrieve user entry after submit clicked. 
    #col2.selectbox("Year: ", years, key="year")

