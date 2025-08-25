import streamlit as st
import numpy as np
import pickle

with open("iris_svm_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌸 Iris Flower Classification using SVM")

sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, value=5.5, step=0.1)
sepal_width  = st.number_input("Sepal Width (cm)", min_value=0.0, value=3.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, value=4.2, step=0.1)
petal_width  = st.number_input("Petal Width (cm)", min_value=0.0, value=1.3, step=0.1)

if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    st.success(f"🌼 Predicted Species: **{prediction}**")