from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the trained model and scaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/sc.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            print("POST request received")  # Debug line
            # Get form data
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = int(request.form.get('Classes'))
            Region = int(request.form.get('Region'))
            
            # Create input array
            input_data = np.array([
                Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region
            ]).reshape(1, -1)
            
            # Scale the input data
            scaled_data = standard_scaler.transform(input_data)
            
            # Make prediction
            prediction = ridge_model.predict(scaled_data)
            
            # Return result
            results = {
                'Predicted FWI': f"{prediction[0]:.2f}",
                'Prediction Value': prediction[0]
            }
            print(f"Prediction successful: {prediction[0]}")  # Debug line
            return render_template('success.html', results=results)
            
        except Exception as e:
            print(f"Error occurred: {str(e)}")  # Debug line
            return render_template('error.html', message=f"An error occurred: {str(e)}")
    else:
        print("GET request received")  # Debug line
        return render_template('home.html')


    



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)


