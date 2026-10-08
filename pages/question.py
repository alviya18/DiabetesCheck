import streamlit as st
import base64


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="DiabetesCheck",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# SESSION STATE
# =========================================================

if "step" not in st.session_state:
    st.session_state.step = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* -----------------------------------------
       PAGE
    ----------------------------------------- */

    .stApp {
        background: #ffffff;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* -----------------------------------------
       LOGO
    ----------------------------------------- */

    .logo {
        text-align: center;
        margin-bottom: 25px;
    }

    .logo img {
        width: 165px;
    }


    /* -----------------------------------------
       PROGRESS
    ----------------------------------------- */

    .progress-text {
        text-align: center;
        color: #6b7280;
        font-size: 14px;
        margin-bottom: 8px;
    }

    .progress-background {
        width: 100%;
        height: 7px;
        background: #e8edf2;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 35px;
    }

    .progress-fill {
        height: 100%;
        background: #4f9fe8;
        border-radius: 20px;
    }


    /* -----------------------------------------
       QUESTION
    ----------------------------------------- */

    .question-number {
        color: #4f9fe8;
        font-size: 14px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 10px;
    }

    .question-title {
        color: #202733;
        font-size: 34px;
        font-weight: 700;
        line-height: 1.25;
        margin-bottom: 10px;
    }

    .question-description {
        color: #6b7280;
        font-size: 16px;
        line-height: 1.5;
        margin-bottom: 30px;
    }


    /* -----------------------------------------
       ANSWER BUTTONS
    ----------------------------------------- */

    div.stButton > button {
    width: 100%;
    min-height: 62px;
    border-radius: 12px;
    border: 1.5px solid #d9dfe6;
    background-color: #ffffff;
    color: #202733;
    font-family: Arial, sans-serif;
    font-size: 16px;
    font-weight: 500;
    transition: all 0.2s ease;
    }

    div.stButton > button,
    div.stButton > button p,
    div.stButton > button span {
        font-family: Arial, sans-serif !important;
    }

    div.stButton > button:hover {
        border-color: #4f9fe8;
        color: #4f9fe8;
        background-color: #f6fbff;
    }


    /* -----------------------------------------
       SELECTED ANSWER
    ----------------------------------------- */

    .selected-answer {
        border: 2px solid #4f9fe8;
        background: #f4faff;
        color: #4f9fe8;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        font-weight: 600;
        margin-bottom: 15px;
    }


    /* -----------------------------------------
       NAVIGATION
    ----------------------------------------- */

    .nav-space {
        margin-top: 35px;
    }


    /* -----------------------------------------
       INPUTS
    ----------------------------------------- */

    div[data-testid="stNumberInput"] input {
        border-radius: 10px;
    }


    /* -----------------------------------------
       HIDE DEFAULT STREAMLIT ELEMENTS
    ----------------------------------------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)



# =========================================================
# QUESTIONS
# =========================================================

questions = [

    {
        "key": "Age",
        "title": "How old are you?",
        "description": "Please select your age group.",
        "type": "choice",
        "options": [
            "18–24",
            "25–29",
            "30–34",
            "35–39",
            "40–44",
            "45–49",
            "50–54",
            "55–59",
            "60–64",
            "65–69",
            "70–74",
            "75–79",
            "80+"
        ]
    },

    {
        "key": "Sex",
        "title": "What is your sex?",
        "description": "Please select an option.",
        "type": "choice",
        "options": [
            "Female",
            "Male"
        ]
    },

    {
        "key": "BodyMeasurements",
        "title": "What are your height and weight?",
        "description": "These values will be used to calculate your BMI.",
        "type": "measurements"
    },

    {
        "key": "HighBP",
        "title": "Have you ever been told that you have high blood pressure?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "HighChol",
        "title": "Have you ever been told that you have high cholesterol?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "CholCheck",
        "title": "Have you checked your cholesterol within the past 5 years?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "Smoker",
        "title": "Have you smoked at least 100 cigarettes in your life?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "Stroke",
        "title": "Have you ever had a stroke?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "HeartDiseaseorAttack",
        "title": "Have you ever had coronary heart disease or a heart attack?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "PhysActivity",
        "title": "Have you participated in physical activity during the past 30 days?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "Fruits",
        "title": "Do you consume fruit regularly?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "Veggies",
        "title": "Do you consume vegetables regularly?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "HvyAlcoholConsump",
        "title": "Do you consume alcohol heavily?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "AnyHealthcare",
        "title": "Do you have any kind of healthcare coverage?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "NoDocbcCost",
        "title": "Was there a time when you needed to see a doctor but could not because of cost?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "GenHlth",
        "title": "In general, how would you rate your health?",
        "description": "Select the option that best describes your general health.",
        "type": "choice",
        "options": [
            "Excellent",
            "Very good",
            "Good",
            "Fair",
            "Poor"
        ]
    },

    {
        "key": "MentHlth",
        "title": "How many days during the past 30 days was your mental health not good?",
        "description": "Enter a number from 0 to 30.",
        "type": "number"
    },

    {
        "key": "PhysHlth",
        "title": "How many days during the past 30 days was your physical health not good?",
        "description": "Enter a number from 0 to 30.",
        "type": "number"
    },

    {
        "key": "DiffWalk",
        "title": "Do you have serious difficulty walking or climbing stairs?",
        "description": "Please select Yes or No.",
        "type": "choice",
        "options": [
            "Yes",
            "No"
        ]
    },

    {
        "key": "Education",
        "title": "What is your highest level of education?",
        "description": "Please select your highest completed education level.",
        "type": "choice",
        "options": [
            "Never attended school",
            "Elementary school",
            "Some high school",
            "High school graduate",
            "Some college",
            "College graduate"
        ]
    },

    {
        "key": "Income",
        "title": "What is your annual household income?",
        "description": "Please select your income category.",
        "type": "choice",
        "options": [
        "Less than ₹9.67 lakh",
        "₹9.67–₹14.51 lakh",
        "₹14.51–₹19.34 lakh",
        "₹19.34–₹24.18 lakh",
        "₹24.18–₹33.85 lakh",
        "₹33.85–₹48.35 lakh",
        "₹48.35–₹72.53 lakh",
        "₹72.53 lakh or more"
]
    }
]


# =========================================================
# CURRENT QUESTION
# =========================================================

current_step = st.session_state.step
current_question = questions[current_step]

total_questions = len(questions)

progress = (current_step + 1) / total_questions


# =========================================================
# PROGRESS BAR
# =========================================================

st.markdown(
    f"""
    <div class="progress-text"><br>
        Question {current_step + 1} of {total_questions}
    </div>

    <div class="progress-background">
        <div class="progress-fill"
             style="width: {progress * 100}%;">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# QUESTION
# =========================================================

st.markdown(
    f"""
    <div class="question-number">
        QUESTION {current_step + 1}
    </div>

    <div class="question-title">
        {current_question["title"]}
    </div>

    <div class="question-description">
        {current_question["description"]}
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# CHOICE QUESTIONS
# =========================================================

if current_question["type"] == "choice":

    options = current_question["options"]

    # Single-column layout
    # This keeps the option order correct on both desktop and mobile.

    for i, option in enumerate(options):

        is_selected = (
            st.session_state.answers.get(
                current_question["key"]
            ) == option
        )

        button_label = (
            f"✓  {option}"
            if is_selected
            else option
        )

        if st.button(
            button_label,
            key=f"option_{current_step}_{i}",
            use_container_width=True
        ):

            st.session_state.answers[
                current_question["key"]
            ] = option

            st.rerun()


# =========================================================
# HEIGHT + WEIGHT
# =========================================================

elif current_question["type"] == "measurements":

    col1, col2 = st.columns(2)

    with col1:

        height = st.number_input(
            "Height (cm)",
            min_value=50.0,
            max_value=250.0,
            value=st.session_state.answers.get(
                "Height",
                None
            ),
            step=1.0,
            placeholder="Enter your height"
        )

    with col2:

        weight = st.number_input(
            "Weight (kg)",
            min_value=20.0,
            max_value=300.0,
            value=st.session_state.answers.get(
                "Weight",
                None
            ),
            step=1.0,
            placeholder="Enter your weight"
        )

    if height is not None and weight is not None:

        height_m = height / 100

        bmi = weight / (height_m ** 2)

        st.session_state.answers["Height"] = height
        st.session_state.answers["Weight"] = weight
        st.session_state.answers["BMI"] = bmi

# =========================================================
# NUMBER QUESTIONS
# =========================================================

elif current_question["type"] == "number":

    previous = st.session_state.answers.get(
        current_question["key"],
        None
    )

    value = st.number_input(
        "Number of days",
        min_value=0,
        max_value=30,
        value=previous,
        step=1,
        placeholder="Enter number of days"
    )

    if value is not None:

        st.session_state.answers[
            current_question["key"]
        ] = value


# =========================================================
# NAVIGATION
# =========================================================

st.markdown(
    '<div class="nav-space"></div>',
    unsafe_allow_html=True
)

back_col, spacer, next_col = st.columns(
    [1, 2, 1]
)


# =========================================================
# BACK BUTTON
# =========================================================

with back_col:

    if current_step > 0:

        if st.button(
            "← Back",
            use_container_width=True
        ):

            st.session_state.step -= 1

            st.rerun()


# =========================================================
# NEXT BUTTON
# =========================================================

with next_col:

    if current_step < total_questions - 1:

        if st.button(
            "Next →",
            use_container_width=True
        ):

            key = current_question["key"]

            if current_question["type"] == "measurements":

                if (
                    st.session_state.answers.get("Height")
                    is None
                    or
                    st.session_state.answers.get("Weight")
                    is None
                ):

                    st.warning(
                        "Please enter both height and weight."
                    )

                else:

                    st.session_state.step += 1

                    st.rerun()

            elif st.session_state.answers.get(key) is None:

                st.warning(
                    "Please select an answer first."
                )

            else:

                st.session_state.step += 1

                st.rerun()


# =========================================================
# FINAL CHECK
# =========================================================

    else:

        if st.button(
            "Check Result ✓",
            use_container_width=True
        ):

            missing = []

            for question in questions:

                key = question["key"]

                if question["type"] == "measurements":

                    if (
                        st.session_state.answers.get("Height")
                        is None
                        or
                        st.session_state.answers.get("Weight")
                        is None
                    ):

                        missing.append(key)

                elif st.session_state.answers.get(key) is None:

                    missing.append(key)

            if missing:

                st.warning(
                    "Please complete all questions before checking your result."
                )

            else:

                st.session_state["questionnaire"] = (
                    st.session_state.answers.copy()
                )

                st.switch_page("pages/result.py")