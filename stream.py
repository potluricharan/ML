import streamlit as st
import pickle 
import pandas as pd
import numpy as np


teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Kolkata Knight Riders',
    'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals',
    'Punjab Kings', 'Lucknow Super Giants', 'Gujarat Titans',
    'Royal Challengers Bengaluru'
]

venues = [
    'Wankhede Stadium', 'Eden Gardens', 'MA Chidambaram Stadium',
    'Rajiv Gandhi International Stadium', 'M Chinnaswamy Stadium',
    'Sawai Mansingh Stadium', 'Feroz Shah Kotla', 'Dubai International Cricket Stadium',
    'Arun Jaitley Stadium', 'Dr DY Patil Sports Academy',
    'Maharashtra Cricket Association Stadium', 'Punjab Cricket Association Stadium',
    'Narendra Modi Stadium', 'Sheikh Zayed Stadium', 'Sharjah Cricket Stadium',
    'Brabourne Stadium', 'Punjab Cricket Association IS Bindra Stadium',
    'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium',
    'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 'Subrata Roy Sahara Stadium',
    'Kingsmead', 'M.Chinnaswamy Stadium', 'Himachal Pradesh Cricket Association Stadium',
    'Sardar Patel Stadium', 'SuperSport Park', 'Maharaja Yadavindra Singh International Cricket Stadium',
    'Saurashtra Cricket Association Stadium', 'Holkar Cricket Stadium', 'New Wanderers Stadium',
    'Zayed Cricket Stadium', 'Barabati Stadium', "St George's Park",
    'JSCA International Stadium Complex ', 'Newlands', 'Shaheed Veer Narayan Singh International Stadium',
    'Barsapara Cricket Stadium', 'Nehru Stadium', 'Green Park',
    'Vidarbha Cricket Association Stadium', 'De Beers Diamond Oval', 'Buffalo Park', 'OUTsurance Oval'
]

pipe=pickle.load(open('pipe.pkl','rb'))
st.title("IPL score predictor")


col1, col2 = st.beta_columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team',teams)

with col2:
    bowling_team = st.selectbox('Select Bowling Team', teams)

# Fixed: uses 'venues' list and stores choice in 'selected_venue'
selected_venue = st.selectbox('Select Venue', venues)

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score', min_value=0)
with col4:
    over_done = st.number_input('Overs Done (e.g., 5.4)', min_value=0.1, max_value=20.0)
with col5:
    last_five = st.number_input('Runs scored in last 5 overs', min_value=0)

# 4. Prediction Logic
if st.button('Predict Score'):
    # Feature Engineering to match pipe.pkl
    overs_completed = int(over_done)
    balls_in_current_over = int(round((over_done % 1) * 10))
    balls_bowled = (overs_completed * 6) + balls_in_current_over
    balls_left = 120 - balls_bowled
    
    # Calculate Current Run Rate (named 'curr' in your model)
    curr = current_score / over_done if over_done > 0 else 0

    # Create input dataframe
    # Your pipe.pkl requires these 12 columns in this specific order
    input_df = pd.DataFrame({
        'ball': [over_done],
        'total_runs': [current_score],
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'venue': [selected_venue],
        'team1': [batting_team],
        'team2': [bowling_team],
        'current_score': [current_score],
        'balls_bowled': [balls_bowled],
        'balls_left': [balls_left],
        'curr': [curr],
        'last_five': [last_five]
    })

    # Predict and Display
    try:
        result = pipe.predict(input_df)
        st.header(f"Predicted Final Score: {int(result[0])}")
    except Exception as e:
        st.error(f"Prediction Error: {e}")