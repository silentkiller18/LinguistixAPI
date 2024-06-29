from flask import Flask, request, jsonify
from transformers import pipeline
from langdetect import detect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# Authentication decorator
def require_auth(func):
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth or not (auth.username == 'user' and auth.password == 'password'):
            return jsonify({"message": "Authentication required"}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

# Specifying models for pipelines
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# Helper function to check language
def check_language(text):
    try:
        language = detect(text)
        return language == 'en'
    except Exception as e:
        app.logger.error(f"Error detecting language: {str(e)}")
        return False

@app.route('/sentiment', methods=['POST'])
@require_auth
@limiter.limit("10 per minute")
def sentiment():
    try:
        data = request.json
        app.logger.debug(f"Received input for sentiment: {data}")
        if not data:
            return jsonify({"message": "No data provided"}), 400
        text = data.get('text')
        if not text:
            return jsonify({"message": "No text provided"}), 400
        if not check_language(text):
            return jsonify({"message": "Only English text is supported"}), 400
        result = sentiment_pipeline(text)
        return jsonify(result)
    except Exception as e:
        app.logger.error(f"Error processing sentiment request: {str(e)}")
        return jsonify({"message": "Error processing request"}), 500

@app.route('/summarize', methods=['POST'])
@require_auth
@limiter.limit("10 per minute")
def summarize():
    try:
        data = request.json
        app.logger.debug(f"Received input for summarization: {data}")
        if not data:
            return jsonify({"message": "No data provided"}), 400
        text = data.get('text')
        if not text:
            return jsonify({"message": "No text provided"}), 400
        if not check_language(text):
            return jsonify({"message": "Only English text is supported"}), 400
        result = summarization_pipeline(text)
        return jsonify(result)
    except Exception as e:
        app.logger.error(f"Error processing summarization request: {str(e)}")
        return jsonify({"message": "Error processing request"}), 500

if __name__ == '__main__':
    app.run(debug=True)
