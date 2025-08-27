import pickle
import numpy as np
import streamlit as st

with open("iris_svm_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="🌸 Iris Flower Classifier", page_icon="🌼", layout="centered")

st.title("🌸 Iris Flower Classification (SVM)")
st.write("Enter the flower measurements below to predict its **species**.")

with st.form("iris_form"):
    st.subheader("📋 Enter Flower Measurements")
    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.number_input("Sepal length (cm)", 4.0, 8.5, 5.5, step=0.1)
        petal_length = st.number_input("Petal length (cm)", 1.0, 7.0, 4.2, step=0.1)
    with col2:
        sepal_width  = st.number_input("Sepal width (cm)", 2.0, 5.0, 3.0, step=0.1)
        petal_width  = st.number_input("Petal width (cm)", 0.1, 2.5, 1.3, step=0.1)
    submitted = st.form_submit_button("🔍 Predict Species")

if submitted:
    X_new = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(X_new)[0]
    species = ["Setosa 🌱", "Versicolor 🌸", "Virginica 🌷"][prediction]
    st.success(f"### 🌼 Predicted Species: **{species}**")
    st.write("#### 🔎 Input Summary")
    st.table({
        "Feature": ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"],
        "Value (cm)": [sepal_length, sepal_width, petal_length, petal_width]
    })
