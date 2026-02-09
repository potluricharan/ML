# import streamlit as st
# import pickle 
# import pandas as pd
# import numpy as np

# # Load the pipeline safely
# try:
#     with open('pipe.pkl', 'rb') as f:
#         pipe = pickle.load(f)
# except Exception as e:
#     st.error(f"Error loading model: {e}")

# st.title("IPL Score Predictor")

# # Data definitions
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

# # UI Layout
# col1, col2 = st.columns(2)

# with col1:
#     batting_team = st.selectbox('Select Batting Team', sorted(teams))
# with col2:
#     bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

# selected_venue = st.selectbox('Select Venue', sorted(venues))

# col3, col4, col5 = st.columns(3)

# with col3:
#     current_score = st.number_input('Current Score', min_value=0, step=1)
# with col4:
#     # Changed step to 0.1 and ensured it's treated as a float
#     over_done = st.number_input('Overs Done (e.g., 5.4)', min_value=0.0, max_value=20.0, step=0.1)
# with col5:
#     last_five = st.number_input('Runs in last 5 overs', min_value=0, step=1)

# # Prediction Logic
# if st.button('Predict Score'):
#     # 1. Feature Engineering
#     # Converting to float to avoid type errors in the pipeline
#     over_done = float(over_done)
    
#     overs_completed = int(over_done)
#     balls_in_current_over = int(round((over_done % 1) * 10))
    
#     total_balls_bowled = (overs_completed * 6) + balls_in_current_over
#     balls_left = 120 - total_balls_bowled
    
#     # Calculate Run Rate
#     crr = current_score / over_done if over_done > 0 else 0

#     # 2. Create input DataFrame in the STRICT order expected by pipe.pkl
#     # The order MUST be: ball, total_runs, current_score, balls_bowled, balls_left, curr, last_five, 
#     # batting_team, bowling_team, venue, team1, team2
#     input_df = pd.DataFrame({
#         'ball': [float(over_done)],
#         'total_runs': [float(current_score)],
#         'current_score': [float(current_score)],
#         'balls_bowled': [float(total_balls_bowled)],
#         'balls_left': [float(balls_left)],
#         'curr': [float(crr)],
#         'last_five': [float(last_five)],
#         'batting_team': [batting_team],
#         'bowling_team': [bowling_team],
#         'venue': [selected_venue],
#         'team1': [batting_team],
#         'team2': [bowling_team]
#     })

#     # 3. Final Prediction
#     try:
#         prediction = pipe.predict(input_df)
#         final_score = int(prediction[0])
        
#         st.success(f"Predicted Final Score: {final_score}")
#     except Exception as e:
#         st.error(f"An error occurred: {e}")
#         st.write("Ensure your input matches the training categories.")

# import streamlit as st
# import pickle 
# import pandas as pd
# import numpy as np
# import traceback

# # Load the pipeline
# try:
#     with open('pipe.pkl', 'rb') as f:
#         pipe = pickle.load(f)
# except Exception as e:
#     st.error(f"Error loading model: {e}")

# st.title("IPL Score Predictor")

# # Data definitions - Cleaned to match model training
# teams = [
#     'Sunrisers Hyderabad', 'Mumbai Indians', 'Kolkata Knight Riders',
#     'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals',
#     'Punjab Kings', 'Lucknow Super Giants', 'Gujarat Titans',
#     'Royal Challengers Bengaluru'
# ]

# # Cleaned venue list (removed duplicates and trailing spaces)
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
#     'Kingsmead', 'Himachal Pradesh Cricket Association Stadium',
#     'Sardar Patel Stadium', 'SuperSport Park', 'Maharaja Yadavindra Singh International Cricket Stadium',
#     'Saurashtra Cricket Association Stadium', 'Holkar Cricket Stadium', 'New Wanderers Stadium',
#     'Zayed Cricket Stadium', 'Barabati Stadium', "St George's Park",
#     'JSCA International Stadium Complex', 'Newlands', 'Shaheed Veer Narayan Singh International Stadium',
#     'Barsapara Cricket Stadium', 'Nehru Stadium', 'Green Park',
#     'Vidarbha Cricket Association Stadium', 'De Beers Diamond Oval', 'Buffalo Park', 'OUTsurance Oval'
# ]

# # UI Layout
# col1, col2 = st.columns(2)

# with col1:
#     batting_team = st.selectbox('Select Batting Team', sorted(teams))
# with col2:
#     bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

# selected_venue = st.selectbox('Select Venue', sorted(venues))

# col3, col4, col5 = st.columns(3)

# with col3:
#     current_score = st.number_input('Current Score', min_value=0, step=1)
# with col4:
#     over_done = st.number_input('Overs Done (e.g., 10.5)', min_value=0.0, max_value=20.0, step=0.1)
# with col5:
#     last_five = st.number_input('Runs in last 5 overs', min_value=0, step=1)

# # Prediction Logic
# if st.button('Predict Score'):
#     try:
#         # 1. Feature Engineering
#         # Ensure floating point types for the model
#         over_done_f = float(over_done)
#         current_score_f = float(current_score)
#         last_five_f = float(last_five)
        
#         # Calculate balls bowled and left
#         overs_int = int(over_done_f)
#         balls_in_over = int(round((over_done_f % 1) * 10))
#         total_balls_bowled = float((overs_int * 6) + balls_in_over)
#         balls_left = float(120 - total_balls_bowled)
        
#         # Calculate Run Rate (CRR)
#         crr = current_score_f / over_done_f if over_done_f > 0 else 0.0

#         # 2. Create input DataFrame in the EXACT order expected by pipe.pkl
#         # The internal order of your model is: 
#         # Numerical: ball, total_runs, current_score, balls_bowled, balls_left, curr, last_five
#         # Categorical: batting_team, bowling_team, venue, team1, team2
#         input_data = {
#             'ball': [over_done_f],
#             'total_runs': [current_score_f],
#             'current_score': [current_score_f],
#             'balls_bowled': [total_balls_bowled],
#             'balls_left': [balls_left],
#             'curr': [float(crr)],
#             'last_five': [last_five_f],
#             'batting_team': [batting_team],
#             'bowling_team': [bowling_team],
#             'venue': [selected_venue],
#             'team1': [batting_team],
#             'team2': [bowling_team]
#         }
        
#         input_df = pd.DataFrame(input_data)

#         # 3. Explicitly Re-order columns to ensure no mismatch
#         cols_order = [
#             'ball', 'total_runs', 'current_score', 'balls_bowled', 'balls_left', 
#             'curr', 'last_five', 'batting_team', 'bowling_team', 'venue', 
#             'team1', 'team2'
#         ]
#         input_df = input_df[cols_order]

#         # 4. Final Prediction
#         prediction = pipe.predict(input_df)
#         final_score = int(prediction[0])
        
#         st.success(f"Predicted Final Score: {final_score}")
        
#     except Exception as e:
#         st.error(f"Prediction Error: {e}")
#         # Optional: Print the full traceback for debugging if it still fails
#         # st.text(traceback.format_exc())

import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="IPL Predictor")
st.title("IPL Score Predictor")

# 1. Load the pipeline with a check
pipe = None

if os.path.exists('pipe.pkl'):
    try:
        with open('pipe.pkl', 'rb') as f:
            pipe = pickle.load(f)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.info("This often happens if your scikit-learn version is different from the one used to train the model.")
else:
    st.error("File 'pipe.pkl' not found! Please ensure the file is in the same folder as this script.")

# --- Data Definitions ---
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
    'Kingsmead', 'Himachal Pradesh Cricket Association Stadium',
    'Sardar Patel Stadium', 'SuperSport Park', 'Maharaja Yadavindra Singh International Cricket Stadium',
    'Saurashtra Cricket Association Stadium', 'Holkar Cricket Stadium', 'New Wanderers Stadium',
    'Zayed Cricket Stadium', 'Barabati Stadium', "St George's Park",
    'JSCA International Stadium Complex', 'Newlands', 'Shaheed Veer Narayan Singh International Stadium',
    'Barsapara Cricket Stadium', 'Nehru Stadium', 'Green Park',
    'Vidarbha Cricket Association Stadium', 'De Beers Diamond Oval', 'Buffalo Park', 'OUTsurance Oval'
]

# --- UI Layout ---
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
    over_done = st.number_input('Overs Done (e.g., 10.5)', min_value=0.0, max_value=20.0, step=0.1)
with col5:
    last_five = st.number_input('Runs in last 5 overs', min_value=0, step=1)

# --- Prediction Logic ---
if st.button('Predict Score'):
    # Check if pipe exists before using it
    if pipe is None:
        st.error("Cannot predict because the model (pipe.pkl) failed to load. Check the error message at the top.")
    else:
        try:
            # Feature Engineering
            over_done_f = float(over_done)
            current_score_f = float(current_score)
            last_five_f = float(last_five)
            
            overs_int = int(over_done_f)
            balls_in_over = int(round((over_done_f % 1) * 10))
            total_balls_bowled = float((overs_int * 6) + balls_in_over)
            balls_left = float(120 - total_balls_bowled)
            crr = current_score_f / over_done_f if over_done_f > 0 else 0.0

            # Create input DataFrame
            input_df = pd.DataFrame({
                'ball': [over_done_f],
                'total_runs': [current_score_f],
                'current_score': [current_score_f],
                'balls_bowled': [total_balls_bowled],
                'balls_left': [balls_left],
                'curr': [float(crr)],
                'last_five': [last_five_f],
                'batting_team': [batting_team],
                'bowling_team': [bowling_team],
                'venue': [selected_venue],
                'team1': [batting_team],
                'team2': [bowling_team]
            })

            # Re-order columns
            cols_order = [
                'ball', 'total_runs', 'current_score', 'balls_bowled', 'balls_left', 
                'curr', 'last_five', 'batting_team', 'bowling_team', 'venue', 
                'team1', 'team2'
            ]
            input_df = input_df[cols_order]

            # Prediction
            prediction = pipe.predict(input_df)
            st.success(f"Predicted Final Score: {int(prediction[0])}")
            
        except Exception as e:
            st.error(f"Prediction Error: {e}")