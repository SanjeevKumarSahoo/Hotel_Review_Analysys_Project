# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:28:37 2024

@author: Admin
"""

import streamlit as st
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import TfidfTransformer
import joblib

# Function to load the pre-trained SVM model

def load_model():
    # Load your pre-trained SVM model here
    svm_model = joblib.load('E:/DATA SCIENCE/Project/Hotel Review Analysis/svm_linear.pkl', 'rb')
    tfidfVectorizer = joblib.load('E:/DATA SCIENCE/Project/Hotel Review Analysis/tfidf_vectorizer.pkl', 'rb')

    return svm_model, tfidfVectorizer
    

# Function to make predictions and extract keywords

def analyze_review(model, vectorizer, text):
    sentiment_prediction = model.predict(vectorizer.transform([text]))[0]

    # Extracting keywords using TF-IDF
    tfidf_matrix = vectorizer.transform([text])
    feature_names = vectorizer.get_feature_names_out()
    keywords = [feature_names[i] for i in tfidf_matrix.indices]

    return sentiment_prediction, keywords

# Streamlit UI
def main():
    st.title("Hotel Review Analysis - Sentiment and Keywords")
    st.sidebar.header("User Input")

    # Get user input
    user_review = st.sidebar.text_area("Enter your hotel review:")

    # Load the SVM model
    svm_model, tfidf_vectorizer = load_model()

    if st.sidebar.button("Analyze Review"):
        # Make sentiment prediction and extract keywords
        sentiment_prediction, keywords = analyze_review(svm_model, tfidf_vectorizer, user_review)

        # Display results
        st.write("Sentiment:", "Positive" if sentiment_prediction == 1 else "Negative")
        st.write("Keywords:", ", ".join(keywords))

if __name__ == "__main__":
    main()