"""
A Flask application for emotion detection using the
Watson NLP library, deployed on localhost:5000.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Endpoint to detect emotions from a given text.

    Receives a text input via query parameters, processes it using the
    emotion_detector function, and returns the detected emotions.

    Returns:
        str: A formatted string containing the emotions and their scores,
        or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please provide a valid input."

    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text! Please provide a valid input."

    emotions = [
        f"'{emotion}': {score}"
        for emotion, score in response.items()
        if emotion != 'dominant_emotion'
    ]
    result = (
        f"For the given statement, the system detected the following emotions: "
        f"{', '.join(emotions)}. The dominant emotion is {dominant_emotion}."
    )

    return result

@app.route('/')
def index():
    """
    Renders the main HTML page.

    Returns:
        str: The rendered HTML content for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

