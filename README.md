# 📊 Customer Churn Prediction

## 📌 Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses. This project aims to predict whether a customer is likely to churn using machine learning techniques.

The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model comparison, hyperparameter tuning, threshold tuning, and deployment using Streamlit.

---

## 🎯 Problem Statement

The objective is to predict customer churn based on customer demographics, account information, services subscribed, billing information, and contract details.

Early identification of customers likely to churn helps businesses take proactive retention measures.

---

## Deployment Link 
https://customer-churn-prediction-project-xtqbshprjuzjdykkiycxnh.streamlit.app/

---

## 📂 Dataset

Dataset: IBM Telco Customer Churn Dataset

Features include:

* Customer demographics
* Internet services
* Contract type
* Billing information
* Payment methods
* Customer tenure

Target Variable:

* **Churn**

  * 0 → Customer stays
  * 1 → Customer churns

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Streamlit
* Joblib

---

## 📈 Exploratory Data Analysis

Performed:

* Churn distribution analysis
* Correlation analysis
* Feature relationship visualization
* Missing value analysis
* Data type inspection

---

## ⚙️ Data Preprocessing

Steps performed:

* Converted TotalCharges to numeric
* Handled missing values
* Encoded categorical variables
* Feature engineering
* Train-test split
* Feature scaling where required

---

## 🤖 Models Trained

The following machine learning models were trained and evaluated:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Decision Tree
4. Random Forest
5. Gradient Boosting
6. AdaBoost
7. Support Vector Classifier (SVC)
8. XGBoost

---

## 📊 Model Evaluation

Evaluation metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

### Model Comparison

| Model               | Accuracy | ROC-AUC |
| ------------------- | -------- | ------- |
| Logistic Regression | 79.53%   | 0.847   |
| Gradient Boosting   | 80.05%   | 0.841   |
| AdaBoost            | 79.29%   | 0.840   |
| Random Forest       | 78.91%   | 0.816   |
| XGBoost             | 77.49%   | 0.811   |
| SVC                 | 79.24%   | 0.804   |
| KNN                 | 75.59%   | 0.766   |
| Decision Tree       | 73.03%   | 0.669   |

---

## 🔧 Hyperparameter Tuning

Hyperparameter tuning was performed using RandomizedSearchCV.

Best Gradient Boosting Parameters:

```python
{
    'subsample': 1.0,
    'n_estimators': 100,
    'max_depth': 3,
    'learning_rate': 0.05
}
```

---

## 📉 Threshold Tuning

The default threshold of 0.5 was adjusted to 0.3 to improve churn detection.

Results:

* Accuracy: 75.59%
* F1 Score: 62.55%
* Recall: 77%

This helped identify significantly more customers at risk of churning.

---

## 📈 ROC Curve

Final Model ROC-AUC Score:
![alt text](image-1.png)

**0.841**

The model demonstrates strong ability to distinguish between churn and non-churn customers.

---

## 🚀 Streamlit Deployment

The trained model was deployed using Streamlit to allow users to enter customer information and receive churn predictions in real time.

Features:

* Interactive UI
* Real-time predictions
* Churn probability estimation

--- 

## 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── datasets/
├── images/
├── notebooks/
│
├── app.py
├── churn_model.pkl
├── features.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 💡 Key Insights

* Contract type is a strong indicator of churn.
* Customers with shorter tenure are more likely to churn.
* Customers using month-to-month contracts show higher churn rates.
* Internet service and payment methods influence churn behavior.
* Threshold tuning significantly improved churn detection.

---

## 🔮 Future Improvements

* SMOTE for class imbalance handling
* Advanced ensemble models
* Explainable AI using SHAP
* Docker deployment
* Cloud deployment using AWS/GCP/Azure

---

## 👩‍💻 Author

**Karra Harshita**

Electronics and Telecommunication Engineering Student

Passionate about Machine Learning, Data Science, and Software Development.
