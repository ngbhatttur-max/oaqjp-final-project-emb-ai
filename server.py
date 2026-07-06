from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    # Handle both POST (form submission) and GET (query string)
    if request.method == "POST":
        text_to_analyze = request.form.get("text", "")
    else:  # GET request
        text_to_analyze = request.args.get("textToAnalyze", "")

    # Run emotion detection
    result = emotion_detector(text_to_analyze)

    # Format response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
