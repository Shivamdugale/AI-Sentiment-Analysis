# 🤖 AI Sentiment Analysis

An AI-powered Sentiment Analysis web application that predicts whether a movie review is **Positive** or **Negative** using **Natural Language Processing (NLP)** and **Machine Learning**.

---

## 📌 Project Overview

This project uses the IMDb Movie Reviews dataset to train a Machine Learning model that classifies user reviews into positive or negative sentiments.

The application is deployed using **Streamlit**, allowing users to enter a review and instantly receive the predicted sentiment along with the confidence score.

---

## 🚀 Features

- Predicts Positive or Negative sentiment
- Confidence score for every prediction
- Interactive Streamlit web application
- Text preprocessing and cleaning
- TF-IDF Vectorization
- Logistic Regression Classifier
- Trained on 50,000 IMDb movie reviews

---

## 📂 Dataset

- **Dataset:** IMDb Movie Reviews Dataset
- **Total Reviews:** 50,000
- **Classes:**
  - Positive
  - Negative

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLP
- TF-IDF Vectorizer
- Logistic Regression
- Joblib
- Streamlit

---

## 🤖 Machine Learning Workflow

1. Import Dataset
2. Data Cleaning
3. Text Preprocessing
4. TF-IDF Feature Extraction
5. Train-Test Split
6. Logistic Regression Training
7. Model Evaluation
8. Save Model
9. Streamlit Deployment

---

## 📊 Model Performance

- **Algorithm:** Logistic Regression
- **Feature Extraction:** TF-IDF Vectorizer
- **Accuracy:** **89.72%**

---

## 📁 Project Structure

```
AI-Sentiment-Analysis/
│
├── dataset/
│   └── IMDB Dataset.csv
│
├── models/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── app.py
├── Sentiment_Analysis.ipynb
├── README.md
└── requirements.txt
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Sentiment-Analysis.git
```

Move into the project

```bash
cd AI-Sentiment-Analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 👨‍💻 Author

**Shivam Dugale**

- GitHub: https://github.com/Shivamdugale
- LinkedIn: https://www.linkedin.com/in/shivam-dugale-782468239/

---

⭐ If you found this project helpful, don't forget to star the repository!