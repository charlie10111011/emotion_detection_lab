import json
import requests

def emotion_detector(text_to_analyze):  # Define the emotion detection function that takes the string input
   # Emotion detection service URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   # Create a dictionary of the input string
    myobj = { "raw_document": { "text": text_to_analyze } }
   # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   # Send a POST request to the API with the string and header
    response = requests.post(url, json = myobj, headers=header) 
   # Assign the status code to a variable
    status_code = response.status_code

   # Parse the JSON response 
    formatted_response = json.loads(response.text)

   # Create a dictionary for the response
    emotion_dict = {}
   
   # Generate the formatted response
    if status_code == 200:
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion_score = max(emotion_dict['anger'], emotion_dict['disgust'], emotion_dict['fear'], emotion_dict['joy'], emotion_dict['sadness'])
        dominant_emotion = ''
        if dominant_emotion_score == emotion_dict['anger']:
            dominant_emotion = 'anger'
        elif dominant_emotion_score == emotion_dict['disgust']:
            dominant_emotion = 'disgust'
        elif dominant_emotion_score == emotion_dict['fear']:
            dominant_emotion = 'fear'
        elif dominant_emotion_score == emotion_dict['joy']:
            dominant_emotion = 'joy'
        elif dominant_emotion_score == emotion_dict['sadness']:
            dominant_emotion = 'sadness'
    elif status_code == 400:
        emotion_dict['anger'] = None
        emotion_dict['disgust'] = None
        emotion_dict['fear'] = None
        emotion_dict['joy'] = None
        emotion_dict['sadness'] = None
        emotion_dict['dominant_emotion'] = None
    
    return emotion_dict
