import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# 1.Title and Subheader
st.title("Data Analysis")
st.subheader("Data analysis using python and straemlit")
# 2.Upload Dataset
upload=st.file_uploader("upload you data set in CSV format")
if upload is not None:
    data=pd.read_csv(upload)
# 3.Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
# 4. Check DataType of Each Column
if upload is not None:
    if st.checkbox("Datatypes of each columns"):
        st.text("Data types")
        st.write(data.dtypes)
# 5. Find Shape of Our Dataset (Number of Rows And Number of Columns)       
if upload is not None:
    data_shape=st.radio("what shape yoy wanna see?",("Rows","Columns"))
    if data_shape=='Rows':
        st.text('Number of Rows')
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text('Number of Columns')
        st.write(data.shape[1])
# 6.Find Null Values in The Dataset       
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("check whether dataset having null or not"):
            fig, ax = plt.subplots()
            ax=sns.heatmap(data.isnull())
            st.pyplot(fig)
    else:
        st.success("congrats, no missing values")
    
# 7. Find Duplicate Values in the dataset   
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("you have duplicate values in data set")
        dup=st.selectbox("do you want to remove duplicate?",("select one","yes","no"))
        if dup=="yes":
            data=data.drop_duplicates()
            st.text('duplicate values are removed')
        if dup=="no":
            st.text('no issues')
            
            
                

