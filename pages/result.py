import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64
import re
from pathlib import Path


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="DiabetesCheck Result",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "random_forest.pkl"
LOGO_PATH = BASE_DIR / "assets" / "images" / "DiabetesCheckLogo.png"


# =========================================================
# LOAD LOGO BASE64 FOR WATERMARK
# =========================================================

logo_base64 = ""
if LOGO_PATH.exists():
    with open(LOGO_PATH, "rb") as f:
        logo_base64 = base64.b64encode(f.read()).decode()


# =========================================================
# PAGE CSS (BRIGHTER BACKGROUND & REORDERED RESULT LAYOUT)
# =========================================================

st.markdown(f"""
<style>
/* App background watermark with higher brightness/lower opacity */
.stApp {{
    background-image: linear-gradient(rgba(255, 255, 255, 0.80), rgba(255, 255, 255, 0.80)), url("data:image/png;base64,{logo_base64}");
    background-repeat: no-repeat;
    background-position: center;
    background-size: 650px auto;
    height: 100vh;
    overflow: hidden;
}}

/* Hide Streamlit elements */
#MainMenu {{ visibility: hidden; }}
footer {{ visibility: hidden; }}
header {{ visibility: hidden; }}

/* True dead-center positioning using absolute transform */
.block-container {{
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    max-width: 900px !important;
    width: 100% !important;
    padding: 0rem !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
}}

/* Centered borderless result container */
.result-container {{
    text-align: center;
    padding: 20px 10px;
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
}}

.result-label {{
    color: #526b86;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1.2px;
    margin-bottom: 15px;
}}

.probability-text {{
    font-size: 25px;
    font-weight: 600;
    color: #334155;
    margin-bottom: 10px;
}}

.result-statement {{
    font-size: 60px;
    font-weight: 800;
    margin-bottom: 30px;
}}

.diabetic-text {{
    color: #ef4444; /* Vibrant Red */
}}

.not-diabetic-text {{
    color: #22c55e; /* Vibrant Green */
}}

.disclaimer {{
    border: 1px solid #f3cccc;
    border-radius: 12px;
    padding: 18px 25px;
    color: #c0392b;
    font-size: 14px;
    font-weight: 500;
    line-height: 1.6;
    text-align: center;
    max-width: 750px;
    margin: 0 auto;
}}
</style>
""", unsafe_allow_html=True)


# =========================================================
# CHECK QUESTIONNAIRE DATA
# =========================================================

if "questionnaire" not in st.session_state:
    st.error("No questionnaire data found.")
    st.stop()

answers = st.session_state["questionnaire"]


# =========================================================
# LOAD RANDOM FOREST MODEL
# =========================================================

try:
    loaded_model = joblib.load(MODEL_PATH)

    if isinstance(loaded_model, dict):
        model = loaded_model["model"]
        saved_features = loaded_model.get("feature_names", None)
    else:
        model = loaded_model
        saved_features = None

except Exception as e:
    st.error("There was a problem loading the Random Forest model.")
    st.code(str(e))
    st.stop()


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def yes_no(value):
    if isinstance(value, bool):
        return 1 if value else 0
    value = str(value).strip().lower()
    if value in ["yes", "y", "true", "1"]:
        return 1
    if value in ["no", "n", "false", "0"]:
        return 0
    return int(float(value))


def convert_age(value):
    if isinstance(value, (int, float, np.integer, np.floating)):
        value = int(value)
        if 1 <= value <= 13:
            return value

    value = str(value).strip()
    age_mapping = {
        "18-24": 1, "18 – 24": 1, "18–24": 1,
        "25-29": 2, "25 – 29": 2, "25–29": 2,
        "30-34": 3, "30 – 34": 3, "30–34": 3,
        "35-39": 4, "35 – 39": 4, "35–39": 4,
        "40-44": 5, "40 – 44": 5, "40–44": 5,
        "45-49": 6, "45 – 49": 6, "45–49": 6,
        "50-54": 7, "50 – 54": 7, "50–54": 7,
        "55-59": 8, "55 – 59": 8, "55–59": 8,
        "60-64": 9, "60 – 64": 9, "60–64": 9,
        "65-69": 10, "65 – 69": 10, "65–69": 10,
        "70-74": 11, "70 – 74": 11, "70–74": 11,
        "75-79": 12, "75 – 79": 12, "75–79": 12,
        "80+": 13, "80 +": 13
    }
    if value in age_mapping:
        return age_mapping[value]
    raise ValueError(f"Unknown age category: {value}")


def convert_sex(value):
    if isinstance(value, (int, float, np.integer, np.floating)):
        value = int(value)
        if value in [0, 1]:
            return value
    value = str(value).strip().lower()
    if value == "female":
        return 0
    if value == "male":
        return 1
    raise ValueError(f"Unknown sex value: {value}")


def convert_general_health(value):
    if isinstance(value, (int, float, np.integer, np.floating)):
        value = int(value)
        if 1 <= value <= 5:
            return value
    value = str(value).strip().lower()
    mapping = {
        "excellent": 1,
        "very good": 2,
        "good": 3,
        "fair": 4,
        "poor": 5
    }
    if value in mapping:
        return mapping[value]
    raise ValueError(f"Unknown general health value: {value}")


def convert_education(value):
    if isinstance(value, (int, float, np.integer, np.floating)):
        value = int(value)
        if 1 <= value <= 6:
            return value
    value = str(value).strip().lower()
    mapping = {
        "never attended school": 1,
        "elementary": 2,
        "high school": 3,
        "some college": 4,
        "college graduate": 6,
        "college graduate or above": 6
    }
    if value in mapping:
        return mapping[value]
    if "college graduate" in value:
        return 6
    if "some college" in value:
        return 4
    if "high school" in value:
        return 3
    if "elementary" in value:
        return 2
    if "never" in value:
        return 1
    raise ValueError(f"Unknown education value: {value}")


# =========================================================
# INCOME CONVERSION
# =========================================================

INR_PER_USD = 96.76

def income_from_numeric_monthly(monthly_inr):
    monthly_inr = float(monthly_inr)
    annual_inr = monthly_inr * 12
    annual_usd = annual_inr / INR_PER_USD
    if annual_usd < 10000: return 1
    elif annual_usd < 15000: return 2
    elif annual_usd < 20000: return 3
    elif annual_usd < 25000: return 4
    elif annual_usd < 35000: return 5
    elif annual_usd < 50000: return 6
    elif annual_usd < 75000: return 7
    else: return 8


def convert_income(value):
    if isinstance(value, (int, float, np.integer, np.floating)):
        return income_from_numeric_monthly(value)

    text = str(value).strip()
    if text.isdigit():
        number = int(text)
        if 1 <= number <= 8:
            return number

    lower = text.lower()
    if "less than" in lower or "below" in lower or "<" in lower:
        return 1
    if "75,000 or more" in lower or "75000 or more" in lower or "75,000+" in lower or "75k+" in lower or "75 lakh" in lower:
        return 8

    if "$10,000" in text and "$15,000" in text: return 2
    if "$15,000" in text and "$20,000" in text: return 3
    if "$20,000" in text and "$25,000" in text: return 4
    if "$25,000" in text and "$35,000" in text: return 5
    if "$35,000" in text and "$50,000" in text: return 6
    if "$50,000" in text and "$75,000" in text: return 7

    lakh_numbers = re.findall(r"(\d+(?:\.\d+)?)\s*(?:lakh|lakhs)", lower)
    if len(lakh_numbers) >= 2:
        upper_lakh = float(lakh_numbers[1])
        if upper_lakh <= 9.676: return 1
        elif upper_lakh <= 14.514: return 2
        elif upper_lakh <= 19.352: return 3
        elif upper_lakh <= 24.190: return 4
        elif upper_lakh <= 33.866: return 5
        elif upper_lakh <= 48.380: return 6
        elif upper_lakh <= 72.570: return 7
        else: return 8

    if len(lakh_numbers) == 1:
        upper_lakh = float(lakh_numbers[0])
        if upper_lakh <= 9.676: return 1
        elif upper_lakh <= 14.514: return 2
        elif upper_lakh <= 19.352: return 3
        elif upper_lakh <= 24.190: return 4
        elif upper_lakh <= 33.866: return 5
        elif upper_lakh <= 48.380: return 6
        elif upper_lakh <= 72.570: return 7
        else: return 8

    cleaned = text.replace("₹", "").replace(",", "").strip()
    try:
        numeric_value = float(cleaned)
        return income_from_numeric_monthly(numeric_value)
    except:
        pass

    raise ValueError(f"Unknown income value: {value}")


# =========================================================
# GET ANSWERS & PREDICT
# =========================================================

try:
    age = convert_age(answers["Age"])
    sex = convert_sex(answers["Sex"])

    height = float(answers["Height"])
    weight = float(answers["Weight"])
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    high_bp = yes_no(answers["HighBP"])
    high_chol = yes_no(answers["HighChol"])
    chol_check = yes_no(answers["CholCheck"])
    smoker = yes_no(answers["Smoker"])
    stroke = yes_no(answers["Stroke"])
    heart_disease = yes_no(answers["HeartDiseaseorAttack"])
    phys_activity = yes_no(answers["PhysActivity"])
    fruits = yes_no(answers["Fruits"])
    veggies = yes_no(answers["Veggies"])
    heavy_alcohol = yes_no(answers["HvyAlcoholConsump"])
    any_healthcare = yes_no(answers["AnyHealthcare"])
    no_doc_cost = yes_no(answers["NoDocbcCost"])
    general_health = convert_general_health(answers["GenHlth"])
    mental_health = float(answers["MentHlth"])
    physical_health = float(answers["PhysHlth"])
    diff_walk = yes_no(answers["DiffWalk"])
    education = convert_education(answers["Education"])
    income = convert_income(answers["Income"])

    model_input = pd.DataFrame({
        "HighBP": [high_bp],
        "HighChol": [high_chol],
        "CholCheck": [chol_check],
        "BMI": [bmi],
        "Smoker": [smoker],
        "Stroke": [stroke],
        "HeartDiseaseorAttack": [heart_disease],
        "PhysActivity": [phys_activity],
        "Fruits": [fruits],
        "Veggies": [veggies],
        "HvyAlcoholConsump": [heavy_alcohol],
        "AnyHealthcare": [any_healthcare],
        "NoDocbcCost": [no_doc_cost],
        "GenHlth": [general_health],
        "MentHlth": [mental_health],
        "PhysHlth": [physical_health],
        "DiffWalk": [diff_walk],
        "Sex": [sex],
        "Age": [age],
        "Education": [education],
        "Income": [income]
    })

    feature_names = [
        "HighBP", "HighChol", "CholCheck", "BMI", "Smoker", "Stroke",
        "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies",
        "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "GenHlth",
        "MentHlth", "PhysHlth", "DiffWalk", "Sex", "Age", "Education", "Income"
    ]

    if saved_features is not None:
        feature_names = saved_features

    model_input = model_input[feature_names]

    prediction = model.predict(model_input)[0]
    probabilities = model.predict_proba(model_input)[0]
    confidence_percentage = probabilities[int(prediction)] * 100

except Exception as e:
    st.error("There was a problem processing your answers.")
    st.code(str(e))
    st.stop()


# =========================================================
# RESULT UI FORMATTING
# =========================================================

if int(prediction) == 1:
    result_statement = "Diabetic"
    text_class = "diabetic-text"
else:
    result_statement = "Non-Diabetic"
    text_class = "not-diabetic-text"


# =========================================================
# RESULT DISPLAY (FULLY CENTERED & REORDERED)
# =========================================================

st.markdown(f"""
<div class="result-container">
    <div class="probability-text">You are {confidence_percentage:.1f}% likely</div>
    <div class="result-statement {text_class}">{result_statement}</div>
    <div class="disclaimer">
        This is a preliminary screening result and not a
        medical diagnosis. Please consult a qualified
        healthcare professional for proper evaluation
        and medical advice.
    </div>
</div>
""", unsafe_allow_html=True)