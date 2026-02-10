import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        N = float(request.form['nitrogen'])
        P = float(request.form['phosphorous'])
        K = float(request.form['potassium'])
        temp = float(request.form['temperature'])
        hum = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rain = float(request.form['rainfall'])

        features = np.array([[N, P, K, temp, hum, ph, rain]])
        pred = model.predict(features)[0]

        result_text = f"Recommended crop for these conditions: {pred}"

    except Exception as e:
        result_text = f"Error while predicting: {str(e)}"

    return render_template('index.html', prediction=result_text)

if __name__ == '__main__':
    app.run(debug=True)
