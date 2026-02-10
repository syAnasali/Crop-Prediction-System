import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# 1. Load the dataset
data = pd.read_csv("Crop_recommendation.csv")

# 2. Select features in the SAME order as the HTML form
X = data[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]
y = data["label"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Save the trained model safely
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# 6. Print accuracy (optional but good)
accuracy = model.score(X_test, y_test)
print("Model trained and saved as model.pkl")
print("Model accuracy:", round(accuracy * 100, 2), "%")
