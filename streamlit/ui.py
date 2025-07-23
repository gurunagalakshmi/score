import streamlit as st
import requests
st.title(" 📑Score Predictor ✅")
study=st.slider("Study Time ",0,10)
atd=st.slider("Attendance Days",0,100)
gen=st.selectbox("Gender",["Male","Female"])
gender=1 if (gen =="Male")else 0
if(st.button("Predict the score")):
    data={
        "study_time":study,
        "attendance":atd,
        "gender_Male":gender
    }
    res=requests.post("https://score-we1s.onrender.com/predict",json=data)
    result=res.json()
    st.write("The Predict Score is ",result['Predicted_score']) 
