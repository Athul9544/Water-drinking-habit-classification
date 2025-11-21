import numpy as np
import streamlit as st
from os import path
import pickle

st.title("Water drinking habit classification")
fname="data.pkl"
with open(path.join(fname),'rb') as f:
    lr=pickle.load(f)

    
glass=st.number_input("Glasses of water per day")
exe=st.number_input("Exercise_level")
temp=st.number_input("URL_Depth")
weight=st.number_input("TinyURL")
age=st.number_input("DNS_Record")
gender=st.number_input("Web_Traffic")

def low():
  print("What to do")
  print("1: Drink water every 1 hour\n2: Keep a water bottle with you \n3: Drink 1–2 glasses after waking up \n4: Eat water-rich foods (cucumber, watermelon, oranges) \n5: Start slowly: add 1 extra glass per day")

def high():
  print("What to do")
  print("1: Do not drink water forcefully\n2: Check urine color (pale yellow = good) \n3: Add electrolytes if sweating a lot \n4: Balance with foods like banana, coconut water, ORS \n5: Keep intake around 2.5–3.5L unless exercising")

def mod():
  print("What to do")
  print("1: Split water evenly: morning–afternoon–evening\n2: Drink more during exercise \n3: Drink 2 glasses in morning, 2 in afternoon, 2 at night \n4: Use lemon water or herbal tea for extra hydration")

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