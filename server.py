from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector") 
def emo_detector(): 

   # Retrieve the text to analyze from the request arguments 
   text_to_analyze = request.args.get('textToAnalyze') 

   # Pass the text to the emotion detector function and store the response 
   response = emotion_detector(text_to_analyze) 

   # Generate the formatted response
   anger_score = response['anger'],
   disgust_score = response['disgust'],
   fear_score = response['fear'],
   joy_score = response['joy'],
   sadness_score = response['sadness'],
   dominant_emotion_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
   if response['anger'] == None:
      dominant_emotion = None
   elif dominant_emotion_score == anger_score:
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
   detector_response = f"""For the given statement, the system response is
    'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, 'sadness': {sadness_score}.
    The dominant emotion is {dominant_emotion}.""" 
   
   if  dominant_emotion == None:
        return "Invalid text! Please try again."
   else:
        return detector_response

@app.route("/") 
def render_index_page(): 

   return render_template('index.html')

if __name__ == "__main__": 
   app.run(host="0.0.0.0", port=5000)
