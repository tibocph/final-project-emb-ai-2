from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector


app = Flask(__name__)

@app.route('/')
def render_index_page():
    return "Welcome to the Emotion Detector! Please use the /emotionDetector route and provide a text parameter. Example: /emotionDetector?text=I am happy"
@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    text_to_analyze = request.args.get('text')
    
    if not text_to_analyze:
        return "Please provide text to analyze! Example: /emotionDetector?text=I am so happy", 400
        
    result = emotion_detector(text_to_analyze)
    
    if "error" in result:
        return jsonify(result), 400
        
    emotions = result["emotionPredictions"][0]["emotion"]
    
    dominant_emotion = max(emotions, key=emotions.get)
    
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. <br><br>"
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )
    
    return response_text

# Run the application on localhost:5000
if __name__ == '__main__':
    print("Starting the Flask server on http://localhost:5000 ...")
    app.run(host="0.0.0.0", port=5000)