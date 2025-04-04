import json
import requests

def emotion_detector(text_to_analyse):  # Define the emotion detection function that takes the string input
   # Emotion detection service URL
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   # Create a dictionary of the input string
   myobj = { "raw_document": { "text": text_to_analyse } }
   # Set the headers required for the API request
   header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   # Send a POST request to the API with the string and header
   response = requests.post(url, json = myobj, headers=header) 

   # Parse the JSON response 
   formatted_response = json.loads(response.text)

   # Generate the formatted response
   anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger'],
   disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust'],
   fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear'],
   joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy'],
   sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness'],
   dominant_emotion_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
   if dominant_emotion_score == anger_score:
      dominant_emotion = 'anger'
   elif dominant_emotion_score == disgust_score:
      dominant_emotion = 'disgust'
   elif dominant_emotion_score == fear_score:
      dominant_emotion = 'fear'
   elif dominant_emotion_score == joy_score:
      dominant_emotion = 'joy'
   elif dominant_emotion_score == sadness_score:
      dominant_emotion = 'sadness'
   
   # Return the response
   emotions_response = {
                        'anger': anger_score,
                        'disgust': disgust_score,
                        'fear': fear_score,
                        'joy': joy_score,
                        'sadness': sadness_score,
                        'dominant_emotion': dominant_emotion
                        }

   return emotions_response 