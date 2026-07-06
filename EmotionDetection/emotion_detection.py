import requests
import json

def emotion_detector(text_to_analyze):
    # Handle blank input before calling API
    if text_to_analyze.strip() == "":
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

    # Handle API error response
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
