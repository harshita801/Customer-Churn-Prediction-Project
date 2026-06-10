import streamlit as st
import pandas as pd
import joblib
# Load model
model = joblib.load("churn_model.pkl")

st.set_page_config(page_title="Customer Churn Prediction")

st.title("📊 Customer Churn Prediction")

# ==========================
# User Inputs
# ==========================

gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.slider("Tenure (Months)", 0, 72, 12)

phone_service = st.selectbox("Phone Service", ["No", "Yes"])
paperless = st.selectbox("Paperless Billing", ["No", "Yes"])

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=50.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

online_security = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

# ==========================
# Prediction
# ==========================

if st.button("Predict Churn"):

    data = {
        'gender': 0,
        'SeniorCitizen': 0,
        'Partner': 0,
        'Dependents': 0,
        'tenure': tenure,
        'PhoneService': 0,
        'PaperlessBilling': 0,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'MultipleLines_No phone service': 0,
        'MultipleLines_Yes': 0,
        'OnlineBackup_No internet service': 0,
        'OnlineBackup_Yes': 0,
        'OnlineSecurity_No internet service': 0,
        'OnlineSecurity_Yes': 0,
        'PaymentMethod_Credit card (automatic)': 0,
        'PaymentMethod_Electronic check': 0,
        'PaymentMethod_Mailed check': 0,
        'StreamingMovies_No internet service': 0,
        'StreamingMovies_Yes': 0,
        'StreamingTV_No internet service': 0,
        'StreamingTV_Yes': 0,
        'TechSupport_No internet service': 0,
        'TechSupport_Yes': 0,
        'Contract_One year': 0,
        'Contract_Two year': 0,
        'InternetService_Fiber optic': 0,
        'InternetService_No': 0,
        'DeviceProtection_No internet service': 0,
        'DeviceProtection_Yes': 0
    }

    # Binary Columns
    data['gender'] = 1 if gender == "Male" else 0
    data['SeniorCitizen'] = 1 if senior == "Yes" else 0
    data['Partner'] = 1 if partner == "Yes" else 0
    data['Dependents'] = 1 if dependents == "Yes" else 0
    data['PhoneService'] = 1 if phone_service == "Yes" else 0
    data['PaperlessBilling'] = 1 if paperless == "Yes" else 0

    # Multiple Lines
    if multiple_lines == "Yes":
        data['MultipleLines_Yes'] = 1
    elif multiple_lines == "No phone service":
        data['MultipleLines_No phone service'] = 1

    # Online Backup
    if online_backup == "Yes":
        data['OnlineBackup_Yes'] = 1
    elif online_backup == "No internet service":
        data['OnlineBackup_No internet service'] = 1

    # Online Security
    if online_security == "Yes":
        data['OnlineSecurity_Yes'] = 1
    elif online_security == "No internet service":
        data['OnlineSecurity_No internet service'] = 1

    # Payment Method
    if payment_method == "Credit card (automatic)":
        data['PaymentMethod_Credit card (automatic)'] = 1
    elif payment_method == "Electronic check":
        data['PaymentMethod_Electronic check'] = 1
    elif payment_method == "Mailed check":
        data['PaymentMethod_Mailed check'] = 1

    # Streaming Movies
    if streaming_movies == "Yes":
        data['StreamingMovies_Yes'] = 1
    elif streaming_movies == "No internet service":
        data['StreamingMovies_No internet service'] = 1

    # Streaming TV
    if streaming_tv == "Yes":
        data['StreamingTV_Yes'] = 1
    elif streaming_tv == "No internet service":
        data['StreamingTV_No internet service'] = 1

    # Tech Support
    if tech_support == "Yes":
        data['TechSupport_Yes'] = 1
    elif tech_support == "No internet service":
        data['TechSupport_No internet service'] = 1

    # Contract
    if contract == "One year":
        data['Contract_One year'] = 1
    elif contract == "Two year":
        data['Contract_Two year'] = 1

    # Internet Service
    if internet_service == "Fiber optic":
        data['InternetService_Fiber optic'] = 1
    elif internet_service == "No":
        data['InternetService_No'] = 1

    # Device Protection
    if device_protection == "Yes":
        data['DeviceProtection_Yes'] = 1
    elif device_protection == "No internet service":
        data['DeviceProtection_No internet service'] = 1

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(
            f"⚠️ Customer is likely to churn\n\nProbability: {probability:.2%}"
    )
    else:
        st.success(
            f"✅ Customer is unlikely to churn\n\nProbability: {probability:.2%}"
    )
    