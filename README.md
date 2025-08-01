# 🔍 Job-to-Job Recommendation System:
A content-based job recommendation system built using **Streamlit**, **TF-IDF**, and **cosine similarity**, designed to help users discover similar jobs based on their current role.

## 🚀 Features:
- Recommend jobs based on job title using:
  - ✅ Stemming
  - ✅ Lemmatization
- View top 5 similar job titles based on TF-IDF text similarity
- Simple and user-friendly web interface built using Streamlit

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- NLTK (for stemming & lemmatization)
- Streamlit (for UI)
- Re (RegEx)
- Difflib
- Pickle
- Numpy

## 🧠 How it Works:
1. Job descriptions and titles are cleaned using NLP (stemming and lemmatization).
2. TF-IDF vectorization is applied to represent job texts numerically.
3. Cosine similarity is used to measure similarity between jobs.
4. The top 5 most similar jobs are returned based on the selected method.

## 📂 Project Structure:
```bash
├── app.py                  # Streamlit application
├── jobs_df.pickle          # Pickled job dataset with processed columns
├── similarity.pickle       # Cosine similarity matrix (stemming)
├── similarity_lem.pickle   # Cosine similarity matrix (lemmatization)
├── requirements.txt        # Python dependencies
```

## 📦 Installation & Usage:
Clone the repo and install the dependencies:

```bash
git clone https://github.com/shubhamtopiyal/job-to-job-recommendation-system.git
cd job-to-job-recommendation-system
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Live Demo:
- Try the app here 👉 [Deployed Link](https://job-to-job-recommendation-system.streamlit.app)  


## 📧 Contact:
Developed by Shubham Topiyal  

📨 shubhamtopiyal0786@gmail.com 

📌 Feel free to reach out for feedback or collaboration!  
