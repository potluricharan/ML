import streamlit as st
import pickle 
import pandas as pd
import pickle
import pandas as pd

# Load the saved pipeline


pipe=pickle.load(open('pipe.pkl','rb'))
teams=['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals',
 'Punjab Kings',
 'Lucknow Super Giants',
 'Gujarat Titans',
 'Royal Challengers Bengaluru']

venues=['Wankhede Stadium'
'Eden Gardens'
'MA Chidambaram Stadium'
'Rajiv Gandhi International Stadium'
'M Chinnaswamy Stadium'
'Sawai Mansingh Stadium'
'Feroz Shah Kotla'
'Dubai International Cricket Stadium'
'Arun Jaitley Stadium'
'Dr DY Patil Sports Academy'
'Maharashtra Cricket Association Stadium'
'Punjab Cricket Association Stadium'
'Narendra Modi Stadium'
'Sheikh Zayed Stadium'
'Sharjah Cricket Stadium'
'Brabourne Stadium'
'Punjab Cricket Association IS Bindra Stadium'
'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium'
'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium'
'Subrata Roy Sahara Stadium'
'Kingsmead'
'M.Chinnaswamy Stadium'
'Himachal Pradesh Cricket Association Stadium'
'Sardar Patel Stadium'
'SuperSport Park'
'Maharaja Yadavindra Singh International Cricket Stadium'
'Saurashtra Cricket Association Stadium'
'Holkar Cricket Stadium'
'New Wanderers Stadium'
'Zayed Cricket Stadium'
'Barabati Stadium'
'St George\'s Park'
'JSCA International Stadium Complex	'
'Newlands'
'Shaheed Veer Narayan Singh International Stadium'
'Barsapara Cricket Stadium'
'Nehru Stadium'
'Green Park'
'Vidarbha Cricket Association Stadium'
'De Beers Diamond Oval'
'Buffalo Park'
'OUTsurance Oval']

st.title('ipl score predictor')

col1,col2=st.beta_columns(2)

with col1:
    batting_team=st.selectbox('select batting team',sorted(teams))
with col2:
    bowling_team=st.selectbox('select bowling team',sorted(teams))  
city=st.selectbox('select venue',sorted(venues))
col3,col4,col5=st.beta_columns(3)
with col3:
    current_score=st.number_input('current score')
with col4:
    over_done=st.number_input('overs done so far')
last_five=st.number_input('runs scored in last 5 overs')
if st.button('predict score'):
    pass

