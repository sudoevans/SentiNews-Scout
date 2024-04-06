# Sentiment Analysis Flask App

This is a Flask web application that performs sentiment analysis on financial news articles. The app uses a pre-trained Convolutional Neural Network (CNN) model to classify the sentiment of the input text as either positive or negative.

## Prerequisites

Before running the app, make sure you have the following prerequisites installed:

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository or download the source code files.

2. Navigate to the project directory:

   ```
   cd /path/to/project
   ```

3. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   ```

   On Windows:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

   On Unix or MacOS:
   ```
   source venv/bin/activate
   ```

   On Windows:
   ```
   venv\Scripts\activate
   ```

5. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask app:

   ```
   python app.py
   ```

   This will start the development server at `http://localhost:5000`.

2. Open your web browser and navigate to `http://localhost:5000`.

3. Enter the URL of the financial news article you want to analyze in the input field.

4. Click the "Analyze" button to perform sentiment analysis on the article.

5. The app will display the predicted sentiment (positive or negative) and save the analysis result in the SQLite database.

6. You can view the analysis history by scrolling down on the same page.

## File Structure

- `app.py`: The main Flask application file.
- `sentiment_analysis_model.h5`: The pre-trained CNN model for sentiment analysis.
- `requirements.txt`: A file listing the required Python packages and their versions.
- `templates/`: A directory containing HTML templates for rendering the web pages.
- `static/`: A directory for static files like CSS and JavaScript (if any).

## Acknowledgments

- The pre-trained CNN model was trained on the [Financial News Sentiment Analysis Dataset](https://www.kaggle.com/datasets/rahul9166/sentiment-analysis-for-financial-news) from Kaggle.
- This project uses the following Python libraries: Flask, Flask-SQLAlchemy, TensorFlow, and other dependencies listed in `requirements.txt`.
```
