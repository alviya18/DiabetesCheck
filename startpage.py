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
# COLOR PALETTE
# =========================================================
#
# Blue        : #4A90E2
# Dark Blue   : #0D2B4D
# Light Blue  : #EAF3FC
# White       : #FFFFFF
# Dark Text   : #263238
# Grey Text   : #667085
#
# =========================================================


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* -----------------------------------------------------
       GENERAL PAGE
    ----------------------------------------------------- */

    .stApp {
        background-color: #FFFFFF;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* -----------------------------------------------------
       HEADER
    ----------------------------------------------------- */

    .logo-header {
        text-align: center;
        margin-top: 25px;
        margin-bottom: 5px;
    }

    .logo-header img {
        width: 210px;
        height: auto;
    }

    .main-subtitle {
        text-align: center;
        color: #263238;
        font-size: 20px;
        margin-bottom: 40px;
    }


    /* -----------------------------------------------------
       START BUTTON
    ----------------------------------------------------- */

    div.stButton {
        margin-top: 25px;
    }

    div.stButton > button {
        height: 52px;

        background-color: #4A90E2;
        color: #FFFFFF;

        border: none;
        border-radius: 8px;

        font-size: 17px;
        font-weight: 600;

        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background-color: #0D2B4D;
        color: #FFFFFF;

        box-shadow: 0 4px 12px rgba(74, 144, 226, 0.20);
    }


    /* -----------------------------------------------------
       SECTION TITLE
    ----------------------------------------------------- */

    .section-title {
        text-align: center;
        color: #4A90E2;
        font-size: 32px;
        font-weight: 650;

        margin-top: 50px;
        margin-bottom: 30px;
    }


    /* -----------------------------------------------------
       FOOTER
    ----------------------------------------------------- */

    .footer {
        text-align: center;
        color: #98A2B3;
        font-size: 13px;

        margin-top: 45px;
        padding-bottom: 20px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD LOGO
# =========================================================

with open(
    "assets/images/DiabetesCheckLogo.png",
    "rb"
) as image_file:

    logo = base64.b64encode(
        image_file.read()
    ).decode()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    f"""
    <div class="logo-header">
        <img
            src="data:image/png;base64,{logo}"
            alt="DiabetesCheck Logo"
        >
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# INTRODUCTION
# =========================================================

st.html("""
<div style="
    background:#FFFFFF;

    padding:38px 55px;

    border-radius:18px;

    border:1px solid #D9EAF8;

    box-shadow:0 5px 20px rgba(74,144,226,0.10);

    text-align:center;

    max-width:850px;

    margin:0 auto;
">

    <div style="
        color:#263238;
        font-size:17px;
        line-height:1.75;
    ">

        <strong style="color:#4A90E2;">
            DiabetesCheck
        </strong>

        is a simple tool that looks at the health and
        lifestyle information you provide and estimates
        whether you may be at risk of having diabetes.

        <br><br>

        It uses a Artificial Intelligence to give you a
        quick screening result that can help you understand
        when you may need to pay more attention to your health.

    </div>

</div>
""")


# =========================================================
# START PREDICTION
# =========================================================

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    if st.button(
        "Start Screening",
        use_container_width=True
    ):
        st.switch_page("pages/question.py")


# =========================================================
# HOW IT WORKS
# =========================================================

st.markdown("""
<div class="section-title">
    How It Works
</div>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)


# =========================================================
# CARD 1
# =========================================================

with col1:

    st.html("""
    <div style="
        background:#FFFFFF;
        padding:20px 25px;
        border-radius:16px;
        height:210px;
        box-sizing:border-box;
        text-align:center;
        border:1px solid #D9EAF8;
        box-shadow:0 4px 15px rgba(74,144,226,0.08);
    ">

        <div style="
            font-size:35px;
            margin-bottom:8px;
        ">
            📋
        </div>

        <div style="
            color:#4A90E2;
            font-size:19px;
            font-weight:600;
            margin-bottom:7px;
        ">
            Answer a Few Questions
        </div>

        <div style="
            color:#667085;
            font-size:14px;
            line-height:1.6;
        ">
            Enter basic information about your health,
            lifestyle, and general well-being.
        </div>

    </div>
    """)


# =========================================================
# CARD 2
# =========================================================

with col2:

    st.html("""
    <div style="
        background:#FFFFFF;
        padding:20px 25px;
        border-radius:16px;
        height:210px;
        box-sizing:border-box;
        text-align:center;
        border:1px solid #D9EAF8;
        box-shadow:0 4px 15px rgba(74,144,226,0.08);
    ">

        <div style="
            font-size:35px;
            margin-bottom:8px;
        ">
            🤖
        </div>

        <div style="
            color:#4A90E2;
            font-size:19px;
            font-weight:600;
            margin-bottom:7px;
        ">
            Get a Screening Result
        </div>

        <div style="
            color:#667085;
            font-size:14px;
            line-height:1.6;
        ">
            Our machine learning model analyses your
            answers and estimates your diabetes status.
        </div>

    </div>
    """)


# =========================================================
# CARD 3
# =========================================================

with col3:

    st.html("""
    <div style="
        background:#FFFFFF;
        padding:20px 25px;
        border-radius:16px;
        height:210px;
        box-sizing:border-box;
        text-align:center;
        border:1px solid #D9EAF8;
        box-shadow:0 4px 15px rgba(74,144,226,0.08);
    ">

        <div style="
            font-size:35px;
            margin-bottom:8px;
        ">
            👨‍⚕️
        </div>

        <div style="
            color:#4A90E2;
            font-size:19px;
            font-weight:600;
            margin-bottom:7px;
        ">
            Confirm With a Doctor
        </div>

        <div style="
            color:#667085;
            font-size:14px;
            line-height:1.6;
        ">
            Use the result only as an initial indication.
            Always consult a doctor for proper diagnosis
            and medical advice.
        </div>

    </div>
    """)


# =========================================================
# BOTTOM DISCLAIMER
# =========================================================

st.html("""
<div style="
    text-align:center;

    background:#F8FAFD;

    padding:18px 25px;

    border-radius:10px;

    margin:40px auto 0 auto;

    max-width:900px;

    color:#667085;

    font-size:13px;

    line-height:1.6;
">

    DiabetesCheck is an educational and screening tool.
    It cannot confirm whether a person has diabetes.
    For an accurate diagnosis, please consult a qualified
    healthcare professional.

</div>
""")


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">
    Developed by Alviya Shibu : )
</div>
""")