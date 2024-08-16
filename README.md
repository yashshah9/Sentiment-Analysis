# 🚀 Sentiment Analysis Web Application

![Status](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.12-blue)

Welcome to the **Sentiment Analysis Web Application**! This Python-based application leverages machine learning models to analyze and predict the sentiment of text input by users. Whether you're curious about how different texts are perceived or looking to incorporate sentiment analysis into your project, this tool is here to help.

## 🌟 Features

- **Model Choice**: Select between Logistic Regression and Neural Network models.
- **Real-Time Sentiment Prediction**: Get instant feedback on whether the sentiment of your text is positive or negative.
- **Simple UI**: Easy-to-navigate interface for a seamless user experience.

## 🛠️ Technology Stack

- **Backend**: Flask
- **Machine Learning**: Scikit-Learn, NLTK
- **Frontend**: HTML, CSS
- **Data Handling**: Joblib for model and vectorizer serialization

## 🚀 Installation

To get this project up and running on your local machine:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yashshah9/Sentiment-Analysis.git
    cd Sentiment-Analysis
    ```

2. **Set Up a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download Models and Vectorizer:**
   - Ensure you have the pre-trained models (`model_lr.pkl`, `model_nn.pkl`) and vectorizer (`vectorizer.pkl`) in the project directory.

5. **Run the Application:**

    ```bash
    python app.py
    ```

6. **Open Your Browser:**

    Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to start using the app.

## 🎯 Usage

1. **Choose a Model**: Pick either Logistic Regression or Neural Network from the dropdown menu.
2. **Enter Text**: Type or paste the text you want to analyze.
3. **Click "Predict"**: Receive instant sentiment analysis and view the result.

## 📊 Example Output

**Model Used:** Logistic Regression  
**Sentiment:** Positive

## 💡 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/YourFeature`).
5. Open a pull request.



Thank you for checking out this project! We hope you find it useful. 🌟
