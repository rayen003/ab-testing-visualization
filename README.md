# A/B Testing Visualization App

This Streamlit app performs A/B testing on two different visualizations to determine which is more effective at answering a business question using the Iris dataset.

## Features
- **A/B Testing**: Randomly displays either a bar chart or box plot
- **Response Time Measurement**: Tracks how long users take to answer
- **Google Sheets Integration**: Pulls data directly from Google Sheets
- **Interactive UI**: Includes animations and progress indicators

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Google Sheets credentials in `credentials.json`
4. Run the app: `streamlit run A1.py`

## Requirements
- Python 3.8+
- Streamlit
- Seaborn
- Pandas
- Gspread
- OAuth2Client

## Deployment Link:
https://ab-testing-visualization.streamlit.app/


