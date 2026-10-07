import streamlit as st

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
# Green      : #198754
# Dark Green : #146C43
# Light Green: #E8F5E9
# Red        : #DC3545
# Light Red  : #FDECEC
# White      : #FFFFFF
# Dark Text  : #263238
# Grey Text  : #667085
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

    .main-title {
        text-align: center;
        color: #198754;
        font-size: 48px;
        font-weight: 700;
        margin-top: 35px;
        margin-bottom: 5px;
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
        display: flex;
        justify-content: center;
        margin-top: 25px;
    }

    div.stButton > button {
        width: 240px;
        height: 52px;

        background-color: #198754;
        color: #FFFFFF;

        border: none;
        border-radius: 8px;

        font-size: 17px;
        font-weight: 600;

        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background-color: #146C43;
        color: #FFFFFF;

        box-shadow: 0 4px 12px rgba(25, 135, 84, 0.20);
    }


    /* -----------------------------------------------------
       SECTION TITLE
    ----------------------------------------------------- */

    .section-title {
        text-align: center;
        color: #198754;
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
# HEADER
# =========================================================

st.markdown("""
<div class="main-title">
    🩺 DiabetesCheck
</div>

<div class="main-subtitle">
    Diabetes Risk Screening 
</div>
""", unsafe_allow_html=True)


# =========================================================
# INTRODUCTION
# =========================================================

st.html("""
<div style="
    background:#FFFFFF;

    padding:38px 55px;

    border-radius:18px;

    border:1px solid #DFF3E7;

    box-shadow:0 5px 20px rgba(25,135,84,0.10);

    text-align:center;

    max-width:850px;

    margin:0 auto;
">

    <div style="
        color:#263238;
        font-size:17px;
        line-height:1.75;
    ">

        <strong style="color:#198754;">
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

if st.button("Start Screening"):

    st.session_state["page"] = "prediction"

    st.rerun()


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

        padding:30px 25px;

        border-radius:16px;

        min-height:185px;

        text-align:center;

        border:1px solid #DFF3E7;

        box-shadow:0 4px 15px rgba(25,135,84,0.08);
    ">

        <div style="
            font-size:35px;
            margin-bottom:12px;
        ">
            📋
        </div>

        <div style="
            color:#198754;
            font-size:19px;
            font-weight:600;
            margin-bottom:10px;
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

        padding:30px 25px;

        border-radius:16px;

        min-height:185px;

        text-align:center;

        border:1px solid #DFF3E7;

        box-shadow:0 4px 15px rgba(25,135,84,0.08);
    ">

        <div style="
            font-size:35px;
            margin-bottom:12px;
        ">
            🤖
        </div>

        <div style="
            color:#198754;
            font-size:19px;
            font-weight:600;
            margin-bottom:10px;
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

        padding:30px 25px;

        border-radius:16px;

        min-height:185px;

        text-align:center;

        border:1px solid #DFF3E7;

        box-shadow:0 4px 15px rgba(25,135,84,0.08);
    ">

        <div style="
            font-size:35px;
            margin-bottom:12px;
        ">
            👨‍⚕️
        </div>

        <div style="
            color:#198754;
            font-size:19px;
            font-weight:600;
            margin-bottom:10px;
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

    background:#F8F9FA;

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