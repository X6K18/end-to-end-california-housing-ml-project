# END-TO-END HOUSING PRICE PREDICTION
A comprehensive machine learning dashboard for predicting house prices in California using multiple models including Linear Regression, Random Forest, XGBoost, and optimized Best XGBoost.

---
## Overview 
This project demonstrates a complete Machine Learning workflow from data preprocessing to model deployment using a modern Flask web application.

The system predicts housing prices based on multiple housing-related features from the California Housing Dataset.

---
## Dashboard 
https://github.com/user-attachments/assets/431827ae-d4d7-41fd-a5e8-ead51a1f08cf

## Features
- California Housing dataset from Scikit-learn
- End-to-end house price prediction
- Flask-based web application
- RESTful API support
- Multiple Machine Learning algorithms
- MLflow experiment tracking
- Dockerized deployment
- Automated logging system
---

## Machine Learning Pipline
### Experimental Setup
- Dataset: California Housing Dataset
- Train/Test Split: 70/30
- Random State: 42
- Feature scaling using StandardScaler for Linear Regression 

### Model Performance

| Model | MSE ↓ | RMSE ↓ | MAE ↓ | R² Score ↑ |
|---|---:|---:|---:|---:|
| Linear Regression (Baseline) | 0.5306 | 0.7284 | 0.5272 | 0.5958 |
| Random Forest (Default) | 0.2545 | 0.5045 | 0.3307 | 0.8061 |
| XGBoost | 0.2041 | 0.4518 | 0.3000 | 0.8445 |
| Random Forest (Tuned) | **0.2000** | **0.4500** | **0.2900** | **0.8500** |

> Lower values are better for MSE, RMSE, and MAE.  
> Higher values are better for R² Score.
---
## Tech Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | Python 3.12, Flask |
| **Machine Learning** | Scikit-learn, XGBoost, Joblib |
| **Data Processing** | Pandas, NumPy |
| **Frontend** | HTML, CSS, JavaScript |
| **Charts** | Chart.js |
| **Icons** | Font Awesome 6 |
| **Tracking** | MLflow |
| **Version Control** | Git, GitHub |


