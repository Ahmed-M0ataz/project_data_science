import numpy as np
from flask import Flask, request, render_template, jsonify
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
feature_order = [
    'hours', 'T6', 'RH_6', 'lights', 'Tdewpoint',
    'Visibility', 'Press_mm_hg', 'Windspeed'
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
# ... other imports ...
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()  # Get form data as a dictionary
    print(data)
    # Convert input data to a numpy array and reshape
    date_string = data['date']
    hour = int(date_string.split("T")[1][:2])  # Extract the hour from the date
    user_input = [hour] + [float(data[feature]) for feature in feature_order[1:]]  # Exclude 'hours'
    
    # Set fixed values for 'low_consum' and 'high_consum'
    low_consum = 1
    high_consum = 0
    
    # Calculate 'hour*lights' and add to the user input
    hour_lights = user_input[feature_order.index('lights')] * hour
    user_input.append(hour_lights)
    print (user_input)
    user_input = [
        low_consum,  # Set your value for low_consum
        high_consum,  # Set your value for high_consum
        hour,
        float(data['T6']),
        float(data['RH_6']),
        int(data['lights']),
        hour * int(data['lights']),  # Calculate and add 'hour*lights'
        float(data['Tdewpoint']),
        float(data['Visibility']),
        float(data['Press_mm_hg']),
        float(data['Windspeed'])
    ]

    user_input_array = np.array(user_input).reshape(1, -1)
    print('user data is ****************')
    print(user_input_array)
    # Load StandardScaler and transform data
    scaler = joblib.load('scaler_95.pkl')
    scaled_input = scaler.transform(user_input_array)

    # Load your pre-trained machine learning model
    random_model = joblib.load('random_model_log_95.pkl')

    # Predict using the model
    prediction_log = random_model.predict(scaled_input)

    # Inverse log transformation
    prediction = np.exp(prediction_log)
    print("the prediction is :***********")
    
    print(prediction_log)
    # Create a response to send back to the website
    response = {'prediction': prediction[0]}
    print(response)
    return jsonify(response)

@app.route('/help')
def help():
    return render_template('help.html')
if __name__ == '__main__':
    app.run(port=3000, debug=True)
