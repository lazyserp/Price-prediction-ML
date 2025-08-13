from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/predict', methods=["POST"])
def predict():
    # Get input from form
    sqft = float(request.form['sqft_living'])
    bed = float(request.form['bedrooms'])
    bath = float(request.form['bathrooms'])
    floors = float(request.form['floors'])
    year = float(request.form['yr_built'])

    # Predict
    input_features = np.array([[sqft, bed, bath, floors, year]])
    prediction = model.predict(input_features)[0]

    return f"<h3>Predicted Price: ₹{int(prediction):,}</h3>"

if __name__ == "__main__":
    app.run(debug=True)
