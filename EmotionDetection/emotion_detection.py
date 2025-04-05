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
   nlp_emotion_response = {}
   
   # Generate the formatted response
   if status_code == 200:
        nlp_emotion_response = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(nlp_emotion_response.items(), key=lambda x: x[1])
        nlp_emotion_response['dominant_emotion'] = dominant_emotion[0]
   elif status_code == 400:
        nlp_emotion_response['anger'] = None
        nlp_emotion_response['disgust'] = None
        nlp_emotion_response['fear'] = None
        nlp_emotion_response['joy'] = None
        nlp_emotion_response['sadness'] = None
        nlp_emotion_response['dominant_emotion'] = None
    
   return nlp_emotion_response
