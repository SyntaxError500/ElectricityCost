# Electricity Cost Prediction 
# link - https://electricitycost.onrender.com

 predict electricity cost using environmental, structural, and utility features. Built with scikit-learn and deployed using FastAPI.

---

##  Exploratory Data Analysis (EDA)

**Key Insights:**

- Mixed-use and Residential are the most common structure types.
- Positive correlations observed between `site_area`, `utilisation_rate`, `resident_count`, and `electricity_cost`.
- Electricity cost is right-skewed.
- Outliers in `water_consumption` and `air_qality_index` retained.

---

##  Feature Preprocessing

**Feature Groups:**

- Categorical: `structure_type`
- Numeric: `site_area`, `water_consumption`, `recycling_rate`, `utilisation_rate`, `air_qality_index`, `issue_reolution_time`, `resident_count`

**Preprocessing:**

- Numeric features scaled using `StandardScaler`
- `structure_type` encoded using `OneHotEncoder`
- Handled via `ColumnTransformer`

---

## Model Selection

**Models Tested:**

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor 
- Gradient Boosting

**Final Model:** `RandomForestRegressor`

- High accuracy
- Robust to outliers
- Best balance of bias and variance


##  API Endpoints

###  `GET /`

**Description:** Test route for API status

json
{
  "message": "Electricity Cost Prediction API is running"
}


###  `POST /predict`

**Description:** Predicts electricity cost from input features

**Request Body Example:**

json
{
  "site_area": 1500,
  "water_consumption": 2300.0,
  "recycling_rate": 65,
  "utilisation_rate": 50,
  "air_qality_index": 180,
  "issue_reolution_time": 2,
  "resident_count": 80,
  "structure_type": "Residential"
}


**Response:**

json
{
  "predicted_cost": 1398.4
}

Valid values for `structure_type`: `"Residential"`, `"Commercial"`, `"Industrial"`, `"Mixed-use"`

## Summary

This project predicts electricity cost using a combination of infrastructure and environmental features. It applies robust preprocessing and machine learning techniques and provides a deployable API for production use.

