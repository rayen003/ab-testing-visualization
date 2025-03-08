import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import random

# Set Seaborn theme for better aesthetics
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12})

# Google Sheets connection
url = "https://docs.google.com/spreadsheets/d/1vClBXgWIU1x1wWSnubY8IRjHKiX1n8KsxKrJnxhupEs/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url)

# App title and question
st.title("📊 A/B Testing: Which Chart is Better?")
st.markdown("**Business Question:** Which species has the largest average sepal length?")

# Initialize session state
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "chart_shown" not in st.session_state:
    st.session_state.chart_shown = False
if "response_time" not in st.session_state:
    st.session_state.response_time = None
if "chart_type" not in st.session_state:
    st.session_state.chart_type = None
if "answered" not in st.session_state:
    st.session_state.answered = False

# Function to create charts
def create_chart(chart_type, data):
    if chart_type == "bar":
        plt.figure(figsize=(10, 6))
        ax = sns.barplot(
            x="species", 
            y="sepal_length1", 
            data=data, 
            palette="viridis",
        )
        plt.title("Average Sepal Length by Species", fontsize=16)
        plt.xlabel("Species", fontsize=14)
        plt.ylabel("Average Sepal Length", fontsize=14)
        plt.xticks(rotation=0)
        plt.tight_layout()
        return plt.gcf()
    else:
        plt.figure(figsize=(10, 6))
        ax = sns.boxplot(
            x="species", 
            y="sepal_length1", 
            data=data,
            palette="magma"
        )
        plt.title("Sepal Length Distribution by Species", fontsize=16)
        plt.xlabel("Species", fontsize=14)
        plt.ylabel("Sepal Length", fontsize=14)
        plt.tight_layout()
        return plt.gcf()

# Function to handle the "Show Chart" button click
def show_chart():
    st.session_state.start_time = datetime.now()
    st.session_state.chart_shown = True
    st.session_state.answered = False
    # Randomly select chart type (50/50 chance)
    st.session_state.chart_type = random.choice(["bar", "box"])

# Function to handle the "I answered your question" button click
def record_answer():
    if st.session_state.start_time:
        end_time = datetime.now()
        st.session_state.response_time = (end_time - st.session_state.start_time).total_seconds()
        st.session_state.answered = True


col1, col2 = st.columns([3, 1])
with col1:
    if st.button("🎲 Show Chart", on_click=show_chart):
        pass

# Display chart if it's been shown
if st.session_state.chart_shown:
    with st.spinner("Loading chart..."):
        # Get data from Google Sheets
        try:
            # Show selected chart
            chart = create_chart(st.session_state.chart_type, data)
            if chart:
                st.pyplot(chart)
                
                # Show response button
                if st.button("✅ I answered your question", on_click=record_answer):
                    pass
                    
        except Exception as e:
            st.error(f"Error reading data from Google Sheets: {str(e)}")

# Display response time if answered
if st.session_state.answered:
    st.toast("Great job! 🎉")
    st.snow()
    st.success(f"Your response time was {st.session_state.response_time:.2f} seconds")
    st.balloons()