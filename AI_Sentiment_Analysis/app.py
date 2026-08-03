import streamlit as st
import joblib
import re
import string

# ------------------------------
# Load Model
# ------------------------------
model = joblib.load("models/sentiment_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="AI Sentiment Analysis",
    page_icon="🤖",
    layout="centered"
)

# ------------------------------
# Custom CSS
# ------------------------------
st.markdown("""
<style>
.stApp{
    background-color:#0E1117;
    color:white;
}

h1{
    text-align:center;
    color:#00D4FF;
}

textarea{
    font-size:18px !important;
}

div.stButton > button{
    width:100%;
    height:55px;
    font-size:20px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Cleaning
# ------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ------------------------------
# Prediction
# ------------------------------
def predict(review):
    review = clean_text(review)
    vector = tfidf.transform([review])

    sentiment = model.predict(vector)[0]
    confidence = model.predict_proba(vector).max()

    return sentiment, confidence

# ------------------------------
# UI
# ------------------------------
st.title("🤖 AI Sentiment Analysis")

st.write("Detect whether a movie review is Positive or Negative.")

review = st.text_area("Enter Review")

if st.button("Predict Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a review.")
    else:

        sentiment, confidence = predict(review)

        if sentiment == "positive":
            st.success("😊 Positive")
        else:
            st.error("😞 Negative")

        st.progress(float(confidence))

        st.metric(
            label="Confidence",
            value=f"{confidence*100:.2f}%"
        )