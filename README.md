# 🏠 House Price Prediction with EDA

A beginner-friendly machine learning project that uses Linear Regression to predict house prices based on features like square footage, number of bedrooms, bathrooms, floors, and year built. The project includes Exploratory Data Analysis (EDA) to visualize data trends and model performance.

## 📁 Project Structure

- `house_price_prediction_with_eda.py` — Main Python script performing data loading, EDA, model training, evaluation, and serialization.
- `dataset.xlsx` — Input dataset (not included in this repo for privacy).
- `house_price_model.pkl` — Saved trained model (optional: generated after running the script).

## 🔍 Features

- **EDA** with:
  - Correlation heatmap
  - Price distribution histogram
  - Regression plot for sqft vs price
- **Modeling** using:
  - `LinearRegression` from `scikit-learn`
  - Train-test split (80-20)
  - RMSE evaluation metric
- **Model Export** using `pickle`

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   cd house-price-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your `dataset.xlsx` file in the root directory.

4. Run the script:
   ```bash
   python house_price_prediction_with_eda.py
   ```

## 🧪 Sample Output

- Correlation matrix between numerical features
- Plot: Square footage vs Price
- Root Mean Square Error (RMSE) printed on console
- `house_price_model.pkl` saved for future use

## 📊 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib & Seaborn (for visualization)
- Scikit-learn (for modeling)
- Pickle (for model serialization)

## 📌 Key Learnings

- Linear regression is a simple yet powerful algorithm for regression problems.
- Data visualization plays a vital role in understanding relationships between features.
- EDA helps identify feature relevance and multicollinearity.
- RMSE is a useful metric for evaluating prediction accuracy.

## 🧠 Future Improvements

- Use advanced regression techniques like Ridge, Lasso, or Gradient Boosting
- Add feature engineering steps (e.g., encode categorical variables)
- Deploy the model via a Flask API or Streamlit app