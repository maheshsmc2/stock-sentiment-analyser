# 💬 Sentiment Analyzer (Gradio Web App)

This is a simple machine learning project that classifies text as **positive** or **negative** using **Logistic Regression**. It is built with **Gradio** and deployable to **Hugging Face Spaces**.

---

## 🚀 Live Demo
🔗 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/your-username/sentiment-analyzer) *(replace with your actual link)*

---

## 📦 Features
- Classifies input text as **positive** or **negative**
- Uses **TF-IDF** for text vectorization
- Trained with **Logistic Regression**
- Interactive Gradio web interface
- Deployed on Hugging Face

---

## 🧠 Concepts Learned
- Text preprocessing and cleaning
- TF-IDF vectorization
- Logistic Regression for binary classification
- Gradio app development
- Hugging Face deployment workflow

---

## 📊 Dataset
A small dataset of 10 sample movie reviews with labels:
- Example:
  - "I love this movie!" → **positive**
  - "This was terrible..." → **negative**

Neutral samples are removed for simplicity.

---

## 🔁 ML Pipeline Flow
```text
1. Load and clean dataset
2. Convert text into vectors using TF-IDF
3. Train Logistic Regression model
4. Build prediction function
5. Create Gradio interface
6. Deploy to Hugging Face
```

---

## 💻 Run Locally
```bash
pip install -r requirements.txt
python app.py
```

---

## 📁 File Structure
```
├── app.py                # Main Gradio app
├── sentiment_data.csv    # Sample reviews and labels
├── requirements.txt      # Dependencies
```

---

## 📸 Screenshot
*(Optional: Upload a screenshot of the app and link it here)*

---

## 👤 Author
Built by Mamata *(ChatGPT-powered AI learning journey)*

---

## 📝 License
This project is for educational purposes and is MIT-licensed.
