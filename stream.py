# import streamlit as st
# import pickle 
# import pandas as pd
# import numpy as np
# import os

# st.set_page_config(page_title="IPL Predictor")
# st.title("IPL Score Predictor")

# # 1. Load the pipeline with a check
# pipe = None

# if os.path.exists('pipe.pkl'):
#     try:
#         with open('pipe.pkl', 'rb') as f:
#             pipe = pickle.load(f)
#     except Exception as e:
#         st.error(f"Error loading model: {e}")
#         st.info("This often happens if your scikit-learn version is different from the one used to train the model.")
# else:
#     st.error("File 'pipe.pkl' not found! Please ensure the file is in the same folder as this script.")

# # --- Data Definitions ---
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
#     'Kingsmead', 'Himachal Pradesh Cricket Association Stadium',
#     'Sardar Patel Stadium', 'SuperSport Park', 'Maharaja Yadavindra Singh International Cricket Stadium',
#     'Saurashtra Cricket Association Stadium', 'Holkar Cricket Stadium', 'New Wanderers Stadium',
#     'Zayed Cricket Stadium', 'Barabati Stadium', "St George's Park",
#     'JSCA International Stadium Complex', 'Newlands', 'Shaheed Veer Narayan Singh International Stadium',
#     'Barsapara Cricket Stadium', 'Nehru Stadium', 'Green Park',
#     'Vidarbha Cricket Association Stadium', 'De Beers Diamond Oval', 'Buffalo Park', 'OUTsurance Oval'
# ]

# # --- UI Layout ---
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

# # --- Prediction Logic ---
# if st.button('Predict Score'):
#     # Check if pipe exists before using it
#     if pipe is None:
#         st.error("Cannot predict because the model (pipe.pkl) failed to load. Check the error message at the top.")
#     else:
#         try:
#             # Feature Engineering
#             over_done_f = float(over_done)
#             current_score_f = float(current_score)
#             last_five_f = float(last_five)
            
#             overs_int = int(over_done_f)
#             balls_in_over = int(round((over_done_f % 1) * 10))
#             total_balls_bowled = float((overs_int * 6) + balls_in_over)
#             balls_left = float(120 - total_balls_bowled)
#             crr = current_score_f / over_done_f if over_done_f > 0 else 0.0

#             # Create input DataFrame
#             input_df = pd.DataFrame({
#                 'ball': [over_done_f],
#                 'total_runs': [current_score_f],
#                 'current_score': [current_score_f],
#                 'balls_bowled': [total_balls_bowled],
#                 'balls_left': [balls_left],
#                 'curr': [float(crr)],
#                 'last_five': [last_five_f],
#                 'batting_team': [batting_team],
#                 'bowling_team': [bowling_team],
#                 'venue': [selected_venue],
#                 'team1': [batting_team],
#                 'team2': [bowling_team]
#             })

#             # Re-order columns
#             cols_order = [
#                 'ball', 'total_runs', 'current_score', 'balls_bowled', 'balls_left', 
#                 'curr', 'last_five', 'batting_team', 'bowling_team', 'venue', 
#                 'team1', 'team2'
#             ]
#             input_df = input_df[cols_order]

#             # Prediction
#             prediction = pipe.predict(input_df)
#             st.success(f"Predicted Final Score: {int(prediction[0])}")
            
#         except Exception as e:
#             st.error(f"Prediction Error: {e}")

import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import os
import re

# Set Page Config
st.set_page_config(page_title="IPL Predictor", layout="centered")
st.title("IPL Score Predictor")

# 1. Load the pipeline with a check
pipe = None

if os.path.exists('pipe.pkl'):
    try:
        with open('pipe.pkl', 'rb') as f:
            pipe = pickle.load(f)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.info("Version mismatch? Ensure scikit-learn version matches the training environment.")
else:
    st.error("File 'pipe.pkl' not found! Please place it in the same directory.")

# --- Data Definitions ---
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Kolkata Knight Riders',
    'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals',
    'Punjab Kings', 'Lucknow Super Giants', 'Gujarat Titans',
    'Royal Challengers Bengaluru'
]

raw_venues = [
    'Wankhede Stadium30138', 'Eden Gardens23436', 'MA Chidambaram Stadium22132',
    'Rajiv Gandhi International Stadium19664', 'M Chinnaswamy Stadium19456',
    'Sawai Mansingh Stadium15194', 'Feroz Shah Kotla13950', 'Dubai International Cricket Stadium11229',
    'Arun Jaitley Stadium9043', 'Dr DY Patil Sports Academy8898',
    'Maharashtra Cricket Association Stadium8414', 'Punjab Cricket Association Stadium8266',
    'Narendra Modi Stadium7923', 'Sheikh Zayed Stadium6925', 'Sharjah Cricket Stadium6672',
    'Brabourne Stadium6526', 'Punjab Cricket Association IS Bindra Stadium6210',
    'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium5235',
    'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium4000', 'Subrata Roy Sahara Stadium3825',
    'Kingsmead3643', 'Himachal Pradesh Cricket Association Stadium3457',
    'Sardar Patel Stadium2893', 'SuperSport Park2866', 'Maharaja Yadavindra Singh International Cricket Stadium2561',
    'Saurashtra Cricket Association Stadium2381', 'Holkar Cricket Stadium1965', 'New Wanderers Stadium1940',
    'Zayed Cricket Stadium1874', 'Barabati Stadium1695', "St George's Park1677",
    'JSCA International Stadium Complex1671', 'Newlands1539', 'Shaheed Veer Narayan Singh International Stadium1431',
    'Barsapara Cricket Stadium1223', 'Nehru Stadium1155', 'Green Park921',
    'Vidarbha Cricket Association Stadium742', 'De Beers Diamond Oval726', 'Buffalo Park715', 'OUTsurance Oval500'
]

# Clean stadium names (remove numbers and strip whitespace)
venues = sorted(list(set([re.sub(r'\d+$', '', v).strip() for v in raw_venues])))

# --- UI Layout ---
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

selected_venue = st.selectbox('Select Venue', venues)

col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score', min_value=0, step=1)
with col4:
    over_done = st.number_input('Overs Done (e.g., 10.5)', min_value=0.0, max_value=20.0, step=0.1)
with col5:
    last_five = st.number_input('Runs in last 5 overs', min_value=0, step=1)

# --- Prediction Logic ---
if st.button('Predict Score'):
    if pipe is None:
        st.error("Model not loaded.")
    elif over_done == 0:
        st.warning("Overs must be greater than 0 for a prediction.")
    else:
        try:
            # Calculations
            overs_int = int(over_done)
            balls_in_over = int(round((over_done % 1) * 10))
            total_balls_bowled = (overs_int * 6) + balls_in_over
            balls_left = 120 - total_balls_bowled
            crr = current_score / over_done

            # Create input DataFrame (Ensuring all columns match model expectations)
            input_df = pd.DataFrame({
                'ball': [over_done],
                'total_runs': [float(current_score)],
                'current_score': [float(current_score)],
                'balls_bowled': [float(total_balls_bowled)],
                'balls_left': [float(balls_left)],
                'curr': [float(crr)],
                'last_five': [float(last_five)],
                'batting_team': [batting_team],
                'bowling_team': [bowling_team],
                'venue': [selected_venue],
                'team1': [batting_team],
                'team2': [bowling_team]
            })

            # Prediction
            prediction = pipe.predict(input_df)
            
            # Display results
            st.markdown("---")
            st.header(f"Predicted Final Score: **{int(prediction[0])}**")
            
        except Exception as e:
            st.error(f"Prediction Error: {e}")
            st.info("Check if your model expects exactly these column names and stadium strings.")