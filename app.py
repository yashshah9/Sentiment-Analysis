from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load trained models and vectorizer
model_lr = joblib.load('model_lr.pkl')
model_nn = joblib.load('model_nn.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Initialize counters for positive and negative sentiments
counters = {
    'logistic_regression': {'total': 0, 'positive': 0, 'negative': 0},
    'neural_network': {'total': 0, 'positive': 0, 'negative': 0}
}

@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html is in the templates folder

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    model_choice = data['model']

    processed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([processed_text])
    
    if model_choice == 'logistic_regression':
        prediction = model_lr.predict(vectorized_text)
    elif model_choice == 'neural_network':
        prediction = model_nn.predict(vectorized_text)
    
    sentiment = 'positive' if prediction[0] == 1 else 'negative'
    
    # Update counters for the chosen model
    counters[model_choice]['total'] += 1
    if sentiment == 'positive':
        counters[model_choice]['positive'] += 1
    else:
        counters[model_choice]['negative'] += 1

    # Calculate percentages for the chosen model
    total_predictions = counters[model_choice]['total']
    positive_percentage = (counters[model_choice]['positive'] / total_predictions) * 100
    negative_percentage = (counters[model_choice]['negative'] / total_predictions) * 100
    
    return jsonify({
        'sentiment': sentiment, 
        'positive_percentage': positive_percentage, 
        'negative_percentage': negative_percentage
    })

import re 
import string
from nltk.corpus import stopwords
import nltk

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove user @ references and '#'
    text = re.sub(r'\@\w+|\#', '', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    
    # Optionally: remove numbers
    text = re.sub(r'\d+', '', text)
    
    return text

if __name__ == '__main__':
    app.run(debug=True)
