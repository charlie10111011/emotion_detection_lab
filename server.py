from flask import Flask, render_template, request 

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector") 
def emotion_detector(text_to_analyze): 

   # Retrieve the text to analyze from the request arguments 
   text_to_analyze = request.args.get('textToAnalyze') 

   # Pass the text to the emotion detector function and store the response 
   response = emotion_detector(text_to_analyze) 

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

   # Extract the emotion and score from the response 
   return "For the given statement, the system response is {}.".format(emotions_response) 

@app.route("/") 
def render_index_page(): 

   return render_template('index.html')

if __name__ == "__main__": 
   app.run(host="0.0.0.0", port=5000)