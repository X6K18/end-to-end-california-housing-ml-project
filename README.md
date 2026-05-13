# **END-TO-END HOUSING PRICE PREDICTION**
A comprehensive machine learning dashboard for predicting house prices in California using multiple models including Linear Regression, Random Forest, XGBoost, and optimized Best XGBoost.

---
## 📌 **Overview**
This project demonstrates a complete Machine Learning workflow from data preprocessing to model deployment using a modern Flask web application.

The system predicts housing prices based on multiple housing-related features from the California Housing Dataset.

---
## 📊 **Dashboard** 
https://github.com/user-attachments/assets/431827ae-d4d7-41fd-a5e8-ead51a1f08cf

<p align="center">
  <img 
    width="95%" 
    alt="Dashboard Overview"
    src="https://github.com/user-attachments/assets/acc2cbb1-72b6-4454-96ea-fd856bfc8f5a" 
  />
</p>

<br><br>

<p align="center">
  <img 
    width="95%" 
    alt="Analytics Dashboard"
    src="https://github.com/user-attachments/assets/18fe3546-375a-4a17-9408-52842277b5c4" 
  />
</p>

<br><br>

<p align="center">
  <img 
    width="95%" 
    alt="Sales Dashboard"
    src="https://github.com/user-attachments/assets/8e4eb19c-87cb-4927-b707-25dbdc3413f3" 
  />
</p>

<br><br>

<p align="center">
  <img 
    width="95%" 
    alt="Customer Dashboard"
    src="https://github.com/user-attachments/assets/3371965b-72d3-421a-856c-7f5803437c01" 
  />
</p>

<br><br>

<p align="center">
  <img 
    width="95%" 
    alt="Revenue Dashboard"
    src="https://github.com/user-attachments/assets/95a26907-62d1-47d4-bcb0-6e02d39bfbfc" 
  />
</p>

<br><br>

---
## 🚀 **Features**
- California Housing dataset from Scikit-learn
- End-to-end house price prediction
- Flask-based web application
- RESTful API support
- Multiple Machine Learning algorithms
- MLflow experiment tracking
- Dockerized deployment
- Automated logging system
---

## 🧠 **Machine Learning Pipeline**
### Experimental Setup
- Dataset: California Housing Dataset
- Train/Test Split: 70/30
- Random State: 42
- Feature scaling using StandardScaler for Linear Regression
- Evaluation Metrics:
  - MSE
  - RMSE
  - MAE
  - R² Score
---

### Dataset Feature
| Feature | Description |
|---|---|
| MedInc | Median income in block group |
| HouseAge | Median house age |
| AveRooms | Average number of rooms |
| AveBedrms | Average number of bedrooms |
| Population | Block group population |
| AveOccup | Average house occupancy |
| Latitude | Latitude coordinate |
| Longitude | Longitude coordinate |

---

### Model Performance

| Model | MSE ↓ | RMSE ↓ | MAE ↓ | R² Score ↑ |
|---|---:|---:|---:|---:|
| Linear Regression (Baseline) | 0.5306 | 0.7284 | 0.5272 | 0.5958 |
| Random Forest (Default) | 0.2545 | 0.5045 | 0.3307 | 0.8061 |
| XGBoost | 0.2041 | 0.4518 | 0.3000 | 0.8445 |
| Random Forest (Tuned) | **0.2000** | **0.4500** | **0.2900** | **0.8500** |

### Visualization 

<img width="1000" height="600" alt="Image" src="https://github.com/user-attachments/assets/3a252f59-d0eb-44bb-8b46-e142a827ae8a" />

<img width="1000" height="600" alt="Image" src="https://github.com/user-attachments/assets/8bdb52cf-711d-40db-afd1-93c3491b2e1b" />

<img width="1000" height="600" alt="Image" src="https://github.com/user-attachments/assets/8e8347e4-b82b-4626-acaa-3edeca39f28a" />

<img width="1000" height="600" alt="Image" src="https://github.com/user-attachments/assets/cb67ee2c-d8c6-41eb-8ec1-f2ce1acf503c" />

> Lower values are better for MSE, RMSE, and MAE.  
> Higher values are better for R² Score.
---
## 🧰 **Tech Stack**

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

---
## 🛠️ **Installation**
### Clone Repository
```
git clone git@github.com:X6K18/end-to-end-california-housing-ml-project.git
cd housing-price-prediction
```
---

### Create Virtual Environment
#### Windows
```
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS
```
python3 -m venv venv
source venv/bin/activate
```
---

#### Install Dependencies
```
pip install -r requirements.txt
```
---

## ▶️ Run Application
```
python -m app.main
```
---
## 👨‍💻 Author
Developed by Nguyen Phan





