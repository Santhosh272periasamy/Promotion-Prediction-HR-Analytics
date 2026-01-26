import streamlit as st
import requests

st.set_page_config(
    page_title="Promotion Prediction",
    layout="centered"
)

st.title("📈 Employee Promotion Prediction")
st.write("Predict whether an employee is likely to be promoted.")

API_URL = "http://127.0.0.1:8000/predict"

# -----------------------------
# Input fields
# -----------------------------
department = st.selectbox("Department", [
    "Sales & Marketing", "Operations", "Technology",
    "Analytics", "R&D", "Procurement", "Finance", "HR", "Legal"
])

region = st.selectbox("Region", [f"region_{i}" for i in range(1, 35)])

education = st.selectbox("Education", [
    "Below Secondary", "Bachelor's", "Master's & above"
])

gender = st.radio("Gender", ["m", "f"])

recruitment_channel = st.selectbox(
    "Recruitment Channel",
    ["sourcing", "other", "referred"]
)

no_of_trainings = st.number_input("No. of Trainings", 0, 10, 1)
age = st.number_input("Age", 20, 60, 30)
previous_year_rating = st.slider("Previous Year Rating", 1, 5, 3)
length_of_service = st.number_input("Length of Service", 1, 40, 5)
awards_won = st.selectbox("Awards Won", [0, 1])
avg_training_score = st.slider("Avg Training Score", 40, 100, 70)

# -----------------------------
# Predict
# -----------------------------
if st.button("Predict Promotion"):
    payload = {
        "department": department,
        "region": region,
        "education": education,
        "gender": gender,
        "recruitment_channel": recruitment_channel,
        "no_of_trainings": no_of_trainings,
        "age": age,
        "previous_year_rating": previous_year_rating,
        "length_of_service": length_of_service,
        "awards_won": awards_won,
        "avg_training_score": avg_training_score
    }

    try:
        response = requests.post(API_URL, json=payload)
        st.write("Status code:", response.status_code)
        st.write("Raw response:", response.text)
        result = response.json()

        if result["promotion_prediction"] == 1:
            st.success(
                f"✅ Likely to be Promoted\n\nProbability: {result['promotion_probability']:.2f}"
            )
        else:
            st.warning(
                f"❌ Not Likely to be Promoted\n\nProbability: {result['promotion_probability']:.2f}"
            )

    except Exception as e:
        st.error(f"API Error: {e}")

