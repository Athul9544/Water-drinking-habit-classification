import numpy as np
import streamlit as st
from os import path
import pickle

st.title("Water drinking habit classification")
fname="data.pkl"
with open(fname,'rb') as f:
    lr=pickle.load(f)

    
glass=st.number_input("Glasses of water per day")
exe=st.number_input("Exercise_level")
temp=st.number_input("URL_Depth")
weight=st.number_input("TinyURL")
age=st.number_input("DNS_Record")
gender=st.number_input("Web_Traffic")

def low():
    st.subheader("What to do (LOW DRINKER):")
    st.write("""
    1. Drink water every 1 hour  
    2. Keep a water bottle with you  
    3. Drink 1–2 glasses after waking up  
    4. Eat water-rich foods  
    5. Add one extra glass daily until habit improves
    """)

def high():
    st.subheader("What to do (HIGH DRINKER):")
    st.write("""
    1. Do not drink water forcefully  
    2. Check urine color (pale yellow = good)  
    3. Add electrolytes if sweating  
    4. Balance with foods like banana, coconut water  
    5. Keep intake around 2.5–3.5L unless exercising heavily
    """)

def mod():
    st.subheader("What to do (MODERATE DRINKER):")
    st.write("""
    1. Spread water evenly throughout the day  
    2. Increase intake during exercise  
    3. Drink 2 glasses morning, 2 afternoon, 2 evening  
    4. Use lemon water / herbal tea  
    """)

if st.button("predict") :
    pred=lr.predict(np.array([[glass,exe,temp,weight,age,gender]]))
    if(pred == 0):
     print("HIGH DRINKER")
     high()
    elif(pred == 1):
     print("LOW DRINKER")
     low()
    else:
     print("MODERATE")

     mod()
