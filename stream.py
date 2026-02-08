import streamlit as st
import pickle 
import pandas as pd

# 1. Load the saved pipeline
pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Kolkata Knight Riders',
         'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals',
         'Punjab Kings', 'Lucknow Super Giants', 'Gujarat Titans',
         'Royal Challengers Bengaluru']

venues = ['Wankhede Stadium', 'Eden Gardens', 'MA Chidambaram Stadium',
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
          'Vidarbha Cricket Association Stadium', 'De Beers Diamond Oval', 'Buffalo Park', 'OUTsurance Oval']

st.title('IPL Score Predictor')

# UI Layout
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

selected_venue = st.selectbox('Select Venue', sorted(venues))

col3, col4 = st.columns(2)

with col3:
    current_score = st.number_input('Current Score', min_value=0)
with col4:
    over_done = st.number_input('Overs Done (e.g., 5.4)', min_value=0.0, max_value=20.0)

last_five = st.number_input('Runs scored in last 5 overs', min_value=0)

if st.button('Predict Score'):
    # Logic to calculate features based on your pipe.pkl
    overs_completed = int(over_done)
    # Extracting the ball number (e.g., from 5.4, the '4' is the 4th ball)
    balls_in_current_over = int(round((over_done % 1) * 10))
    
    # Calculate balls_bowled and balls_left
    balls_bowled = (overs_completed * 6) + balls_in_current_over
    balls_left = 120 - balls_bowled
    
    # Calculate Current Run Rate (named 'curr' in your model)
    curr = current_score / over_done if over_done > 0 else 0

    # Create input dataframe - Column names and order MUST match pipe.pkl
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'venue': [selected_venue],
        'current_score': [current_score],
        'balls_bowled': [balls_bowled],
        'balls_left': [balls_left],
        'curr': [curr],
        'last_five': [last_five]
    })

    # Display prediction
    result = pipe.predict(input_df)
    st.header(f"Predicted Score: {int(result[0])}")