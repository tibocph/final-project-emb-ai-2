from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the text provided in the request arguments and return a formatted string."""
    # Retrieve the text to analyze from the request query parameters
    text_to_analyze = request.args.get("textToAnalyze")

    # FIX: Explicitly check if the input is empty or contains only spaces
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    # Run the emotion detection function if text is present
    response = emotion_detector(text_to_analyze)

    # Secondary check: If the backend dictionary returns None for dominant_emotion
    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # If the input is valid and processed, extract scores and emotions
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    # Format the output string exactly as requested by the customer
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response


@app.route("/")
def render_index_page():
    """Render the main HTML interface."""
    try:
        return render_template("index.html")
    except Exception:
        return "Emotion Detector Server is Running."


if __name__ == "__main__":
    # Deploy the application on localhost:5000
    app.run(host="localhost", port=5000, debug=True)