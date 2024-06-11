import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the provided text using the Watson NLP EmotionPredict API.
    Args:
        text_to_analyze (str): The text for which to analyze emotions.
    Returns:
        dict: A dictionary with scores for each emotion and the dominant emotion.
    """

    # API endpoint URL for Watson NLP EmotionPredict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers containing the model ID to be used for emotion prediction
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # JSON payload with the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Send a POST request to the Watson API with the text and headers
    response = requests.post(url, json=input_json, headers=headers)

    # Check if the response status code is 400 (Bad Request)
    if response.status_code == 400:
        # Return a dictionary with None values indicating invalid input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }

    # Parse the JSON response from the API
    response_data = json.loads(response.text)
    
    # Extract the emotion predictions from the response
    emotions = response_data['emotionPredictions'][0]['emotion']
    
    # Determine the dominant emotion by finding the key with the highest value
    dominant_emotion = max(emotions, key=emotions.get)

    # Construct the result dictionary with individual emotion scores and the dominant emotion
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    # Return the result dictionary
    return result
