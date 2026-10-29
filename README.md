<div align="center">

# 🩺 DiabetesCheck

### ML Based Diabetes Disease Prediction System

<br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
<img src="https://img.shields.io/badge/Random%20Forest-Classifier-228B22?style=for-the-badge">
<img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

</div>

---

**DiabetesCheck** is a machine learning based web application designed to perform **diabetes disease prediction** using non invasive indicators.

The project uses the **2021 Behavioral Risk Factor Surveillance System (BRFSS)** dataset and applies data preprocessing, feature selection, class balancing, and machine learning techniques to develop a predictive model.

The trained **Random Forest Classifier** is integrated into a **Streamlit web application**, providing users with a simple interface for entering the required information and obtaining a prediction.

📝 **Note:** DiabetesCheck is an academic project developed for educational purposes. The prediction provided by the system should not be considered a medical diagnosis.

---

## 🧠 Machine Learning Workflow

```text
                    ┌──────────────────────┐
                    │   BRFSS 2021 Data    │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Data Preprocessing   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Random Under-Sampling│
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ 80 : 20 Train/Test   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │  Random Forest       │
                    │     Classifier       │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Model Evaluation     │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Streamlit Web App    │
                    └──────────────────────┘
