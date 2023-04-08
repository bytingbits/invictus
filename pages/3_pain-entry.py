import streamlit as st
import plotly.graph_objects as go 
import calendar
from datetime import datetime 
import pandas as pd
page_title ="invictus"
page_icon = ":shield:"
layout = "wide"
add_emoji= ":pill:"

df = pd.read_csv("samp.csv", index_col=0)

time_of_day=["Morning", "Afternoon", "Evening"]
location=["Neck", "Head", "Back", "Joints"]

st.set_page_config(page_title=page_title, layout=layout, page_icon=page_icon)
st.title(add_emoji+ " add pain record")
"we're sorry to hear that you're in pain, hope you feel better soon!"


def new_form():
    with st.form("entry_form", clear_on_submit=True):
        a1=st.slider("pain intensity (0 indicates no pain, 10 indicates severe pain)", 0, 10, 1)
        a2=st.time_input("duration (how long did the attack last - hh\:mm)")
        a3=st.selectbox("time of day (when)", time_of_day)
        a4=st.selectbox("location (where did you experience pain)", location)
        a5=st.radio("are you menstruating", ["Yes", "No"])
        submitted=st.form_submit_button("save details")
        if submitted: 
            df = pd.read_csv("samp.csv", index_col=0)
            #data={"INTENSITY":a1,"DURATION":a2,"TIME_OF_DAY":a3,"LOCATION":a4,"MENSTRUATION":a5}
            df.loc[len(df.index)]=[a1,a2,a3,a4,a5]
            #df=df.append(pd.DataFrame(data))
            df.to_csv("samp.csv")
            st.write("saved data!")

new_form()


