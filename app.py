import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import gradio as gr

# Load dataset
df = pd.read_csv("sentiment_data.csv")
df = df[df['sentiment'] != 'neutral']  # Remove neutral for binary classification

# Split
X = df['text']
y = df['sentiment']
tfidf = TfidfVectorizer()
X_vec = tfidf.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict function
def predict_sentiment(text):
    vec = tfidf.transform([text])
    return model.predict(vec)[0]

# Interface
iface = gr.Interface(fn=predict_sentiment, inputs="text", outputs="text", title="Sentiment Analyzer")

if __name__ == "__main__":
    iface.launch()
