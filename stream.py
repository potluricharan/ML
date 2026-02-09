# import streamlit as st
# import pickle 
# import pandas as pd
# import numpy as np


# teams = [
#     'Sunrisers Hyderabad', 'Mumbai Indians', 'Kolkata Knight Riders',
#     'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals',
#     'Punjab Kings', 'Lucknow Super Giants', 'Gujarat Titans',
#     'Royal Challengers Bengaluru'
# ]

# venues = [
#     'Wankhede Stadium', 'Eden Gardens', 'MA Chidambaram Stadium',
#     'Rajiv Gandhi International Stadium', 'M Chinnaswamy Stadium',
#     'Sawai Mansingh Stadium', 'Feroz Shah Kotla', 'Dubai International Cricket Stadium',
#     'Arun Jaitley Stadium', 'Dr DY Patil Sports Academy',
#     'Maharashtra Cricket Association Stadium', 'Punjab Cricket Association Stadium',
#     'Narendra Modi Stadium', 'Sheikh Zayed Stadium', 'Sharjah Cricket Stadium',
#     'Brabourne Stadium', 'Punjab Cricket Association IS Bindra Stadium',
#     'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium',
#     'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 'Subrata Roy Sahara Stadium',
#     'Kingsmead', 'M.Chinnaswamy Stadium', 'Himachal Pradesh Cricket Association Stadium',
#     'Sardar Patel Stadium', 'SuperSport Park', 'Maharaja Yadavindra Singh International Cricket Stadium',
#     'Saurashtra Cricket Association Stadium', 'Holkar Cricket Stadium', 'New Wanderers Stadium',
#     'Zayed Cricket Stadium', 'Barabati Stadium', "St George's Park",
#     'JSCA International Stadium Complex ', 'Newlands', 'Shaheed Veer Narayan Singh International Stadium',
#     'Barsapara Cricket Stadium', 'Nehru Stadium', 'Green Park',
#     'Vidarbha Cricket Association Stadium', 'De Beers Diamond Oval', 'Buffalo Park', 'OUTsurance Oval'
# ]

# pipe=pickle.load(open('pipe.pkl','rb'))
# st.title("IPL score predictor")


# col1, col2 = st.beta_columns(2)

# with col1:
#     batting_team = st.selectbox('Select Batting Team',teams)

# with col2:
#     bowling_team = st.selectbox('Select Bowling Team', teams)

# # Fixed: uses 'venues' list and stores choice in 'selected_venue'
# selected_venue = st.selectbox('Select Venue', venues)

# col3, col4, col5 = st.columns(3)

# with col3:
#     current_score = st.number_input('Current Score', min_value=0)
# with col4:
#     over_done = st.number_input('Overs Done (e.g., 5.4)', min_value=0.1, max_value=20.0)
# with col5:
#     last_five = st.number_input('Runs scored in last 5 overs', min_value=0)

# # 4. Prediction Logic
# if st.button('Predict Score'):
#     # Feature Engineering to match pipe.pkl
#     overs_completed = int(over_done)
#     balls_in_current_over = int(round((over_done % 1) * 10))
#     balls_bowled = (overs_completed * 6) + balls_in_current_over
#     balls_left = 120 - balls_bowled
    
#     # Calculate Current Run Rate (named 'curr' in your model)
#     curr = current_score / over_done if over_done > 0 else 0

#     # Create input dataframe
#     # Your pipe.pkl requires these 12 columns in this specific order
#     input_df = pd.DataFrame({
#         'ball': [over_done],
#         'total_runs': [current_score],
#         'batting_team': [batting_team],
#         'bowling_team': [bowling_team],
#         'venue': [selected_venue],
#         'team1': [batting_team],
#         'team2': [bowling_team],
#         'current_score': [current_score],
#         'balls_bowled': [balls_bowled],
#         'balls_left': [balls_left],
#         'curr': [curr],
#         'last_five': [last_five]
#     })

#     # Predict and Display
#     try:
#         result = pipe.predict(input_df)
#         st.header(f"Predicted Final Score: {int(result[0])}")
#     except Exception as e:
#         st.error(f"Prediction Error: {e}")

import streamlit as st
import pickle 
import pandas as pd
import numpy as np

# Load the pipeline
# Ensure pipe.pkl is in the same directory as this script
try:
    pipe = pickle.load(open('pipe.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model file 'pipe.pkl' not found. Please ensure it is in the correct directory.")

st.title("IPL Score Predictor")

# Data definitions
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

# Input Layout
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))

with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

selected_venue = st.selectbox('Select Venue', sorted(venues))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score', min_value=0, step=1)
with col4:
    over_done = st.number_input('Overs Done (e.g., 5.4)', min_value=0.1, max_value=20.0, step=0.1)
with col5:
    last_five = st.number_input('Runs in last 5 overs', min_value=0, step=1)

# Prediction Logic
if st.button('Predict Score'):
    # 1. Feature Engineering
    overs_completed = int(over_done)
    # Extracting balls from the decimal part (e.g., 5.4 -> 4 balls)
    balls_in_current_over = int(round((over_done % 1) * 10))
    
    total_balls_bowled = (overs_completed * 6) + balls_in_current_over
    balls_left = 120 - total_balls_bowled
    
    # Run Rate calculation
    crr = current_score / over_done if over_done > 0 else 0

    # 2. Create input DataFrame in the EXACT order the pipeline expects
    # Order: ball, total_runs, current_score, balls_bowled, balls_left, curr, last_five, 
    #        batting_team, bowling_team, venue, team1, team2
    input_df = pd.DataFrame({
        'ball': [over_done],
        'total_runs': [current_score],
        'current_score': [current_score],
        'balls_bowled': [total_balls_bowled],
        'balls_left': [balls_left],
        'curr': [crr],
        'last_five': [last_five],
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'venue': [selected_venue],
        'team1': [batting_team],
        'team2': [bowling_team]
    })

    # 3. Predict and Display
    try:
        prediction = pipe.predict(input_df)
        final_score = int(prediction[0])
        
        st.markdown("---")
        st.header(f"Predicted Final Score: {final_score}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        st.info("Check if the input categories (teams/venues) match exactly with the training data.")