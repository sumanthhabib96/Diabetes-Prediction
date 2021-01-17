# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:20:31 2020

@author: Krish Naik
"""
# -*- coding: utf-8 -*-
"""
Created on 03/01/2021 18:13:11

@author: Sumanth Habib
"""

import streamlit as st
from PIL import Image
import pandas as pd
import pickle
import datetime

pickle_in=open('diabetes (1).pkl','rb')
rd=pickle.load(pickle_in)

def welcome():
    'Welcome ALL'
    
def diabetes_prediction(no_times_pregnant,glucose_concentration,blood_pressure,
       skin_fold_thickness,serum_insulin,bmi,diabetes_pedigree,
       age):
    prediction=rd.predict([[no_times_pregnant,glucose_concentration,blood_pressure,
       skin_fold_thickness,serum_insulin,bmi,diabetes_pedigree,
       age]])
    print(prediction)
    return prediction

def main():
    st.write("""# Diabetes Prediction
    Predict if someone has Diabetes using Machine Learning!""")
    html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Daibetes Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)       
    image=Image.open('what-is-data-science.jpg')

    st.image(image,caption='ML',use_column_width=True)
    df=pd.read_csv('train.csv')
    df.drop(columns='p_id',axis=0,inplace=True)
    st.subheader('Data Information')
    st.dataframe(df)
    st.subheader('Statistical_description')
    st.write(df.describe())
    st.bar_chart(df.head()['glucose_concentration'])
    st.subheader('User_Input')
    no_times_pregnant=st.number_input('no_times_pregnant,',0,17,3)
    glucose_concentration=st.number_input('glucose_concentration',0,199,117)
    blood_pressure=st.number_input('blood_pressure',0,122,72)
    skin_fold_thickness=st.number_input('skin_fold_thickness',0,99,23)
    serum_insulin=st.number_input('serum_insulin',0.0,846.0,30.0)
    bmi=st.number_input('bmi',0.0,67.3,32.3)
    diabetes_pedigree=st.number_input('diabetes_pedigree',0.0782,2.42,0.3755)
    age=st.number_input('age',21,89,29)
    result=''
    if st.button('Predict'):
       result=diabetes_prediction(no_times_pregnant,glucose_concentration,blood_pressure,
       skin_fold_thickness,serum_insulin,bmi,diabetes_pedigree,age)
       st.success('The output is {}'.format(result))
       st.subheader('0 indicates patient does not have diabetes')
       st.subheader('1 indicated patient has diabetes')
    if st.button('About'):
        st.text('Lets Learn')
        st.text('Created using streamlit app')
if __name__=='__main__':
    main()
            
    












