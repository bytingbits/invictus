import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

page_icon = ":graph:"
layout = "wide"
add_emoji= ":pill:"

st.title(add_emoji+ " insights")
st.subheader("here are your reports!")
df = pd.read_csv('samp.csv')
df_yes=df.query("MENSTRUATION == 'Yes'")
df_no=df.query("MENSTRUATION == 'No'")

morn_men=df_yes.query("TIME_OF_DAY == 'Morning'")
eve_men=df_yes.query("TIME_OF_DAY == 'Evening'")
aft_men=df_yes.query("TIME_OF_DAY == 'Afternoon'")

morn_nmen=df_no.query("TIME_OF_DAY == 'Morning'")
eve_nmen=df_no.query("TIME_OF_DAY == 'Evening'")
aft_nmen=df_no.query("TIME_OF_DAY == 'Afternoon'")

x_ax=["Morning", "Afternoon", "Evening"]; 
fig=plt.figure()
st.header("Average pain intensity not when menstruating")
p1_ht=[morn_men["INTENSITY"].mean(), aft_men["INTENSITY"].mean(), eve_men["INTENSITY"].mean()]; 
p2_ht=[morn_nmen["INTENSITY"].mean(), aft_nmen["INTENSITY"].mean(), eve_nmen["INTENSITY"].mean()]; 
plt.bar(x_ax, p2_ht)
st.pyplot(fig)

plt.clf() 
st.header("Average pain intensity when menstruating")
plt.bar(x_ax, p1_ht, color='r')
st.pyplot(fig)



# Filter data based on MENSTRUATION




plt.show()