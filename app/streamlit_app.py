import streamlit as st

st.set_page_config(
    page_title="Energy Peak Risk Prediction",
    page_icon="⚡"
)

st.title("⚡ Energy Peak Risk Prediction")

st.write("""
This is a demonstration application for the AI/ML Internship Project.

### Project Information

- Problem Type: Regression
- Target Variable: Global_active_power
- Best Model: Gradient Boosting Regressor

This application will be connected to the trained model in future development.
""")

st.info("Demo version - Model prediction is not connected yet.")

st.success("Project setup completed successfully.")