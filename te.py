# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1vClBXgWIU1x1wWSnubY8IRjHKiX1n8KsxKrJnxhupEs/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)
print("___connection___")

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)