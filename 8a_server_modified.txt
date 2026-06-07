"""
This module sets up a Flask web server for the Emotion Detection application.
It defines routes to process text and return emotion scores.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    """
    Renders the main index page.

    Returns:
        str: A welcome message with usage instructions.
    """
    return (
        "Welcome to the Emotion Detector! "
        "Please use the /emotionDetector route and provide a text parameter. "
        "Example: /emotionDetector?text=I am happy"
    )

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Analyzes the user-provided text for emotions.

    Retrieves the 'text' argument from the URL, passes it to the
    emotion_detector function, and formats the output.

    Returns:
        str: Formatted string displaying emotion scores and the dominant emotion,
             or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('text')

    if not text_to_analyze:
        return (
            "Please provide text to analyze! "
            "Example: /emotionDetector?text=I am so happy"
        ), 400

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. <br><br>"
        f"The dominant emotion is <strong>{result['dominant_emotion']}</strong>."
    )

    return response_text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)