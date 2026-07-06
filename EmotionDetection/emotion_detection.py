import requests
import json

def emotion_detector(text_to_analyze):
    # Call the emotion detection API
    if text_to_analyze.strip() == "":
        # Simulate a 400 Bad Request response for blank input
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    response = requests.post(
        "https://sn-ws-emotion-detection.labs.skills.network/emotion_detection",
        json={"text": text_to_analyze}
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Parse JSON response
    result = json.loads(response.text)
    return result
