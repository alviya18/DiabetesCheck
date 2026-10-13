import base64
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="DiabetesCheck Result",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "random_forest.pkl"
LOGO_PATH = BASE_DIR / "assets" / "images" / "DiabetesCheckLogo.png"

logo_base64 = ""

if LOGO_PATH.exists():
  with open(LOGO_PATH, "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode()


st.markdown(
    f"""
<style>
.stApp {{
    background:
        linear-gradient(
            rgba(255, 255, 255, 0.92),
            rgba(255, 255, 255, 0.92)
        ),
        url("data:image/png;base64,{logo_base64}");
    background-repeat: no-repeat;
    background-position: center;
    background-size: 600px auto;
    background-attachment: fixed;
}}

#MainMenu {{ visibility: hidden; }}
footer {{ visibility: hidden; }}
header {{ visibility: hidden; }}

.block-container {{
    max-width: 1250px !important;
    padding-top: 45px !important;
    padding-bottom: 40px !important;
}}

/* Translucent Card to show background image */
.result-card {{
    border: none;
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 4px 20px rgba(15, 23, 42, 0.03);
    height: 100%;
}}

.card-header {{
    color: #64748b;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 14px;
    text-align: center;
}}

.info-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid rgba(241, 245, 249, 0.8);
    font-size: 14px;
}}

.info-label {{
    color: #64748b;
    font-weight: 400;
}}

.info-value {{
    color: #1e293b;
    font-weight: 700;
}}

.bmi-box {{
    background: rgba(248, 250, 252, 0.8);
    border: none;
    border-radius: 12px;
    padding: 14px 16px;
    margin: 15px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
}}

.bmi-title {{
    color: #526b86;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}}

.bmi-value {{
    color: #1e3a5f;
    font-size: 24px;
    font-weight: 800;
    margin-top: 2px;
}}

.bmi-category {{
    font-size: 13px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
}}

.tips-title {{
    font-size: 18px;
    font-weight: 750;
    color: #1e3a5f;
    margin-bottom: 12px;
    margin-top: 20px;
}}

.tip {{
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin: 11px 0;
    color: #475569;
    font-size: 14px;
    line-height: 1.5;
}}

.tip-icon {{
    color: #16a34a;
    font-weight: 800;
    font-size: 15px;
}}

.disclaimer-box {{
    background: #ffffff;
    border: 1.5px solid #dc2626;
    border-radius: 12px;
    padding: 16px;
    color: #991b1b;
    font-size: 12px;
    line-height: 1.6;
    margin-top: 25px;
}}
</style>
""",
    unsafe_allow_html=True,
)


if "questionnaire" not in st.session_state:
  st.error("No questionnaire data found.")
  st.stop()

answers = st.session_state["questionnaire"]

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
  normalized_value = (
      value.replace("–", "-").replace("—", "-").replace(" ", "")
  )
  age_mapping = {
      "18-24": 1,
      "25-29": 2,
      "30-34": 3,
      "35-39": 4,
      "40-44": 5,
      "45-49": 6,
      "50-54": 7,
      "55-59": 8,
      "60-64": 9,
      "65-69": 10,
      "70-74": 11,
      "75-79": 12,
      "80+": 13,
  }
  if normalized_value in age_mapping:
    return age_mapping[normalized_value]
  if value.isdigit() and 1 <= int(value) <= 13:
    return int(value)
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
  mapping = {"excellent": 1, "very good": 2, "good": 3, "fair": 4, "poor": 5}
  if value in mapping:
    return mapping[value]
  raise ValueError(f"Unknown general health value: {value}")


def convert_education(value):
  if isinstance(value, (int, float, np.integer, np.floating)):
    value = int(value)
    if 1 <= value <= 6:
      return value
  value = str(value).strip().lower()
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


def get_bmi_category(bmi_value):
  if bmi_value < 18.5:
    return "Underweight", "#3b82f6"
  elif 18.5 <= bmi_value < 25:
    return "Normal", "#16a34a"
  elif 25 <= bmi_value < 30:
    return "Overweight", "#d97706"
  else:
    return "Obese", "#dc2626"


INR_PER_USD = 96.76


def income_from_numeric_annualy(annual_inr):
  annual_inr = float(annual_inr)
  annual_usd = annual_inr / INR_PER_USD
  if annual_usd < 10000:
    return 1
  elif annual_usd < 15000:
    return 2
  elif annual_usd < 20000:
    return 3
  elif annual_usd < 25000:
    return 4
  elif annual_usd < 35000:
    return 5
  elif annual_usd < 50000:
    return 6
  elif annual_usd < 75000:
    return 7
  else:
    return 8


def convert_income(value):
  if isinstance(value, (int, float, np.integer, np.floating)):
    return income_from_numeric_annualy(value)
  text = str(value).strip()
  if text.isdigit():
    number = int(text)
    if 1 <= number <= 8:
      return number
  return 4


try:
  age = convert_age(answers["Age"])
  sex = convert_sex(answers["Sex"])
  height = float(answers["Height"])
  weight = float(answers["Weight"])
  height_m = height / 100
  bmi = weight / (height_m**2)

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
      "Income": [income],
  })

  feature_names = [
      "HighBP",
      "HighChol",
      "CholCheck",
      "BMI",
      "Smoker",
      "Stroke",
      "HeartDiseaseorAttack",
      "PhysActivity",
      "Fruits",
      "Veggies",
      "HvyAlcoholConsump",
      "AnyHealthcare",
      "NoDocbcCost",
      "GenHlth",
      "MentHlth",
      "PhysHlth",
      "DiffWalk",
      "Sex",
      "Age",
      "Education",
      "Income",
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
# RESULTS & DISPLAY VALUES
# =========================================================

if int(prediction) == 1:
  result_line1 = f"You are {confidence_percentage:.1f}% likely to be"
  result_line2 = "Diabetic"
  text_class = "color: #dc2626;"
  result_message = (
      "The screening model has classified your responses as diabetic. This"
      " result is only a preliminary screening outcome and should not be"
      " considered a medical diagnosis."
  )
  tips = [
      "Maintain a balanced and nutritious diet.",
      (
          "Stay physically active according to your ability and health"
          " condition."
      ),
      "Maintain a healthy body weight.",
      (
          "Monitor blood glucose as advised by a qualified healthcare"
          " professional."
      ),
      "Avoid smoking and limit alcohol consumption.",
      (
          "Discuss this screening result with a qualified healthcare"
          " professional for proper evaluation."
      ),
  ]
else:
  result_line1 = f"You are {confidence_percentage:.1f}% likely to be"
  result_line2 = "Non-Diabetic"
  text_class = "color: #16a34a;"
  result_message = (
      "The screening model has classified your responses as non-diabetic."
      " Continue maintaining healthy lifestyle habits and regular health"
      " check-ups."
  )
  tips = [
      "Continue maintaining a balanced diet.",
      "Stay physically active on a regular basis.",
      "Maintain a healthy body weight.",
      "Avoid smoking and limit alcohol consumption.",
      "Keep track of important health indicators.",
      "Continue regular health check-ups when appropriate.",
  ]

sex_display = str(answers["Sex"]).title()
age_display = str(answers["Age"])
height_display = f"{height:.1f} cm"
weight_display = f"{weight:.1f} kg"
bmi_display = f"{bmi:.1f}"
bmi_category_text, bmi_category_color = get_bmi_category(bmi)

all_inputs = [
    ("Age", age_display),
    ("Sex", sex_display),
    ("Height", height_display),
    ("Weight", weight_display),
    ("High Blood Pressure", str(answers["HighBP"]).title()),
    ("High Cholesterol", str(answers["HighChol"]).title()),
    ("Cholesterol Check", str(answers["CholCheck"]).title()),
    ("Smoking", str(answers["Smoker"]).title()),
    ("Stroke History", str(answers["Stroke"]).title()),
    ("Heart Disease / Attack", str(answers["HeartDiseaseorAttack"]).title()),
    ("Physical Activity", str(answers["PhysActivity"]).title()),
    ("Fruit Consumption", str(answers["Fruits"]).title()),
    ("Vegetable Consumption", str(answers["Veggies"]).title()),
    ("Heavy Alcohol Consumption", str(answers["HvyAlcoholConsump"]).title()),
    ("General Health", str(answers["GenHlth"]).title()),
    ("Mental Health", f"{int(mental_health)} days"),
    ("Physical Health", f"{int(physical_health)} days"),
    ("Difficulty Walking", str(answers["DiffWalk"]).title()),
    ("Education", str(answers["Education"])),
    ("Income", str(answers["Income"])),
]


left_column, right_column = st.columns([1, 1], gap="large")

with left_column:
  with st.container(border=False):
    inputs_rows_html = "".join([
        f'<div class="info-row"><span class="info-label">{label}</span><span'
        f' class="info-value">{val}</span></div>'
        for label, val in all_inputs
    ])

    left_card_html = f"""<div class="result-card"><div class="card-header">YOUR INFORMATION</div><div class="bmi-box"><div><div class="bmi-title">Body Mass Index (BMI)</div><div class="bmi-value">{bmi_display}</div></div><div class="bmi-category" style="color: {bmi_category_color}; border-color: {bmi_category_color};">{bmi_category_text}</div></div>{inputs_rows_html}</div>"""
    st.markdown(left_card_html, unsafe_allow_html=True)

with right_column:
  with st.container(border=False):
    tips_html = "".join([
        f'<div class="tip"><span class="tip-icon">✓</span><span>{tip}</span></div>'
        for tip in tips
    ])

    message_bg = "rgba(255, 245, 245, 0.9)" if int(prediction) == 1 else "rgba(240, 253, 244, 0.9)"
    message_border = "#fecaca" if int(prediction) == 1 else "#bbf7d0"
    message_color = "#991b1b" if int(prediction) == 1 else "#166534"

    right_card_html = f"""<div class="result-card"><div style="text-align: center; font-size: 18px; color: #334155; font-weight: 600; margin-top: 15px;">{result_line1}</div><div style="text-align: center; font-size: 40px; font-weight: 800; margin-top: 5px; margin-bottom: 20px; {text_class}">{result_line2}</div><div style="margin-top: 20px;"><div style="background: {message_bg}; border: 1px solid {message_border}; color: {message_color}; border-radius: 13px; padding: 15px 17px; font-size: 14px; line-height: 1.6;">{result_message}</div></div><div class="tips-title">General Health Tips</div>{tips_html}<div class="disclaimer-box"><strong>Important:</strong> DiabetesCheck provides a preliminary screening result based on the information entered by the user. This result is not a medical diagnosis. Please consult a qualified healthcare professional for proper evaluation and medical advice.</div></div>"""
    st.markdown(right_card_html, unsafe_allow_html=True)