# 🌱 Crop Prediction System

A Machine Learning powered web application that recommends the best crop to grow based on various soil and environmental parameters. This system aids farmers and agriculturalists in making data-driven decisions to maximize yield.

## 🚀 Features

-   **Precision Recommendations:** Uses a trained Machine Learning model to predict the optimal crop.
-   **User-Friendly Interface:** Simple web form to input environmental data (Nitrogen, Phosphorous, Rainfall, pH, etc.).
-   **Instant Results:** Real-time prediction processing.
-   **Data-Driven:** Built upon a comprehensive agricultural dataset.

## 🛠️ Tech Stack

-   **Frontend:** HTML5, CSS3
-   **Backend:** Python, Flask
-   **Machine Learning:** Scikit-learn, Pandas, NumPy
-   **Dataset:** `Crop_recommendation.csv`

## 📂 Directory Structure

```text
CROP_PREDICTION_MODEL/
├── static/
│   └── styles.css          # CSS for styling the web interface
├── templates/
│   └── index.html          # Main HTML page for user input
├── app.py                  # Flask application entry point
├── Crop_recommendation.csv # Dataset used for training
├── model.pkl               # Serialized Machine Learning model
└── model.py                # Script to train and save the model
```

1. Clone the Repository
Bash

git clone [https://github.com/your-username/crop-prediction-model.git](https://github.com/your-username/crop-prediction-model.git)
cd crop-prediction-model
2. Install Dependencies
Ensure you have Python installed. You will likely need the following libraries:

Bash

pip install flask pandas numpy scikit-learn
3. Train the Model (Optional)
If you want to retrain the model or model.pkl is missing:

Bash

python model.py
This will read Crop_recommendation.csv, train the algorithm, and generate a fresh model.pkl file.

4. Run the Application
Start the Flask server:

Bash

python app.py
5. Access the App
Open your web browser and go to: http://127.0.0.1:5000/
