import newspaper
from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import sqlite3

app = Flask(__name__)

# Load the saved Keras model
model = load_model('Model\sentiment_analysis_model.h5')

# Load or initialize your tokenizer
tokenizer = Tokenizer()
max_length = 100  
# Initialize SQLite database
conn = sqlite3.connect('./Database/analyzed_results.db', check_same_thread=False)
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS analyzed_text (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, sentiment TEXT)''')
conn.commit()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Analyze route
@app.route('/analyze', methods=['POST'])
def analyze():
  if request.method == 'POST':
    link = request.form['input_text']
    input_text= get_news(link)
    # Define sentiment thresholds (modify these values if needed)
    POSITIVE_THRESHOLD = 0.5
    NEGATIVE_THRESHOLD = 1 - POSITIVE_THRESHOLD  # Threshold for negative sentiment

    # Load the model
    model = load_model('./Model/sentiment_analysis_model.h5')

    # Tokenize the text
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([input_text])
    text_sequence = tokenizer.texts_to_sequences([input_text])

    # Pad the sequence
    MAX_SEQUENCE_LENGTH = 30
    text_sequence = pad_sequences(text_sequence, maxlen=MAX_SEQUENCE_LENGTH, padding='post')

    # Predict sentiment
    prediction_probs = model.predict(text_sequence)
    print("Prediction Props---------------->>",prediction_probs)
    prediction = 'positive' if prediction_probs[0][0] > POSITIVE_THRESHOLD else (
        'negative' if prediction_probs[0][0] < NEGATIVE_THRESHOLD else 'neutral'
    )

    # Save the analyzed text and sentiment to the database
    c.execute('''INSERT INTO analyzed_text (text, sentiment) VALUES (?, ?)''', (input_text, prediction))
    conn.commit()

    return redirect(url_for('result'))



# Result route
@app.route('/result')
def result():
    # Fetch previously analyzed results from the database
    c.execute('''SELECT * FROM analyzed_text''')
    analyzed_results = c.fetchall()

    return render_template('result.html', analyzed_results=analyzed_results)


#Fetch news from link
def get_news(link):
        # Create a newspaper article object
        article = newspaper.Article(link)

        # Download the article
        article.download()

        # Parse the article
        article.parse()

        # Get the article text
        text = article.text

        return text

# Preprocess function
def preprocess(text):

    return text.lower()


if __name__ == '__main__':
    app.run(debug=True)

