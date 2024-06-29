# LinguistixAPI 🎉📝

![LinguistixAPI](https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif)

LinguistixAPI is a Flask-based RESTful API for sentiment analysis and text summarization. Leveraging state-of-the-art NLP models from Hugging Face Transformers, this API provides robust and efficient text processing services with built-in authentication and rate limiting.

## 🌟 Features

- **Sentiment Analysis**: Analyze the sentiment of English text using advanced NLP models.
- **Text Summarization**: Generate concise summaries of English text.
- **Authentication**: Secure API endpoints with basic authentication.
- **Rate Limiting**: Control API usage with customizable rate limits.
- **Language Detection**: Ensure support for English text processing only.

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **Hugging Face Transformers**
- **NLTK**
- **Flask-Limiter**

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/LinguistixAPI.git
    cd LinguistixAPI
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Set up environment variables for authentication (optional but recommended for security):
    ```bash
    export API_USERNAME='yourusername'
    export API_PASSWORD='yourpassword'
    ```

2. Run the Flask application:
    ```bash
    python app.py
    ```

3. Use the API endpoints for sentiment analysis and text summarization:

    - **Sentiment Analysis**:
        ```bash
        curl -X POST -u yourusername:yourpassword -H "Content-Type: application/json" -d '{"text":"I love using Hugging Face models!"}' http://127.0.0.1:5000/sentiment
        ```

    - **Text Summarization**:
        ```bash
        curl -X POST -u yourusername:yourpassword -H "Content-Type: application/json" -d '{"text":"Hugging Face models provide easy-to-use and powerful tools for natural language processing."}' http://127.0.0.1:5000/summarize
        ```

## 📄 API Documentation

### Endpoints

- **POST /sentiment**
    - **Description**: Analyze the sentiment of the provided text.
    - **Request Body**: 
        ```json
        {
            "text": "Your text here"
        }
        ```
    - **Response**:
        ```json
        [
            {
                "label": "POSITIVE",
                "score": 0.999
            }
        ]
        ```

- **POST /summarize**
    - **Description**: Generate a summary of the provided text.
    - **Request Body**: 
        ```json
        {
            "text": "Your text here"
        }
        ```
    - **Response**:
        ```json
        [
            {
                "summary_text": "Your summarized text here"
            }
        ]
        ```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/silenkiller18/LinguistixAPI/issues).

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the amazing NLP models.
- [Flask](https://flask.palletsprojects.com/) for the lightweight web framework.
- [NLTK](https://www.nltk.org/) for the natural language toolkit.
- [Giphy](https://giphy.com/) for the fun gif.

---

Feel free to customize it further as per your project's requirements.
