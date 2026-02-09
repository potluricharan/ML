from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
pipe = pickle.load(open('pipe.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve data from form
    batting_team = request.form['batting_team']
    bowling_team = request.form['bowling_team']
    venue = request.form['venue']
    current_score = int(request.form['current_score'])
    overs = float(request.form['overs'])
    last_five = int(request.form['last_five'])

    # Calculation logic (same as your Streamlit code)
    balls_bowled = (int(overs) * 6) + int((overs % 1) * 10)
    balls_left = 120 - balls_bowled
    curr = current_score / overs

    # Create DataFrame matching your pipe.pkl
    input_df = pd.DataFrame({
        'ball': [overs], 'total_runs': [current_score],
        'batting_team': [batting_team], 'bowling_team': [bowling_team],
        'venue': [venue], 'team1': [batting_team], 'team2': [bowling_team],
        'current_score': [current_score], 'balls_bowled': [balls_bowled],
        'balls_left': [balls_left], 'curr': [curr], 'last_five': [last_five]
    })

    result = pipe.predict(input_df)
    prediction = int(result[0])

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)