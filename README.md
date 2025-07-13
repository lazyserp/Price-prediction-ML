# 🏡 House Price Prediction Web App

A beginner-friendly Flask web application that predicts house prices using a linear regression model trained on historical housing data. This project includes data preprocessing, exploratory data analysis (EDA), model training, and deployment.

## 📂 Project Structure

```
├── app.py                          # Flask server to handle routing and predictions
├── form.html                      # HTML form to input house features
├── house_price_model.pkl          # Trained linear regression model
├── dataset.xlsx                   # Source dataset used for training
├── house_price_prediction_with_eda.py  # Notebook-style script for EDA + model training
└── README.md
```

## 🚀 Features

- 📈 Trains a regression model using `scikit-learn`
- 🔍 Performs detailed EDA using `pandas`, `matplotlib`, and `seaborn`
- 🧠 Predicts house prices based on 5 input features:
  - Square feet of living area
  - Number of bedrooms
  - Number of bathrooms
  - Number of floors
  - Year built
- 🌐 Flask-based web UI for easy interaction

## 🧪 Model Training

The model was trained using a simple linear regression algorithm with the following features:
- `sqft_living`
- `bedrooms`
- `bathrooms`
- `floors`
- `yr_built`

Evaluation Metric:
- **Root Mean Square Error (RMSE)** is used to evaluate model accuracy.

See [`house_price_prediction_with_eda.py`](house_price_prediction_with_eda.py) for full training and visualization code.

## 🌐 Web Interface

The web UI (`form.html`) allows users to input house details and view the predicted price.

## 🔧 How to Run

### 🐍 Requirements

Make sure Python 3.7+ is installed. Then install dependencies:

```bash
pip install flask pandas numpy matplotlib seaborn scikit-learn openpyxl
```

### ▶️ Start the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

## 📥 Example Inputs

| Feature       | Example |
|---------------|---------|
| Sqft Living   | 1800    |
| Bedrooms      | 3       |
| Bathrooms     | 2       |
| Floors        | 1       |
| Year Built    | 2010    |

## 📊 Model Performance

The trained model achieves an RMSE of approximately **<your-RMSE-here>** on the test set. You can improve it further using more advanced models or feature engineering.

## 📌 Future Improvements

- Use a more robust model (e.g., XGBoost or Random Forest)
- Add support for categorical features like location or condition
- Improve UI with Tailwind/Bootstrap
- Host the model on cloud (e.g., Render, Heroku, or AWS)

## 📜 License

This project is open source under the [MIT License](LICENSE).
