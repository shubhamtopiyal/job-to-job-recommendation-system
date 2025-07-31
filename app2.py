import streamlit as st
import pandas as pd
import pickle
# using fuzzy string matching to find the closest match along with Lemmatization approach:
from difflib import get_close_matches

# Set page configuration
st.set_page_config(page_title="Job Recommender", page_icon="💼")

# Load data and models
jobs_df = pickle.load(open('jobs_df.pickle', 'rb'))
similarity = pickle.load(open('similarity.pickle', 'rb'))
similarity_lem = pickle.load(open('similarity_lem.pickle', 'rb'))

# Title and description
st.title("🔍 Job Recommendation System")
st.write("Find your next job based on your current skills or job role.")

# Recommendation functions
def recommendation(title):
    try:
        idx = jobs_df[jobs_df['Title'] == title].index[0]
        distances = sorted(list(enumerate(similarity[idx])), key=lambda x: x[1], reverse=True)[1:6]
        return [jobs_df.iloc[i[0]]['Original_Title'] for i in distances]
    except:
        return []

def lem_recommendation(title):
    try:
        idx = jobs_df[jobs_df['Title'] == title].index[0]
        distances = sorted(list(enumerate(similarity_lem[idx])), key=lambda x: x[1], reverse=True)[1:6]
        return [jobs_df.iloc[i[0]]['Original_Title'] for i in distances]
    except:
        return []

# Engine selector
engine = st.selectbox("Choose Recommendation Method:", ["Lemmatization", "Stemming"])
st.write('🧠 Lemmatization-based (Smarter, More Accurate) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🔍 Stemming-based (Faster, Less Precise)')

# Input field
title = st.selectbox("Select your job title:", jobs_df['Title'].unique())

# Recommendation trigger
if st.button("🔎 Recommend Jobs"):

    if engine == "Stemming":
        results = recommendation(title)
    else:
        results = lem_recommendation(title)

    st.markdown("### 📋 Top 5 Recommended Jobs:")
    if results:
        for i, job in enumerate(results, 1):
            st.write(f"{i}. {job}")
        st.success("Recommendations generated successfully!")
    else:
        st.warning("⚠️ No recommendations found for the selected job title.")

st.divider()
st.markdown("📌 **Note**: This app uses a content-based filtering approach using TF-IDF and cosine similarity.")
st.markdown("👨‍💻 Developed by [Shubham Topiyal](mailto:shubhamtopiyal0786@gmail.com)")
