""" Python script for flask web application to run emotion detection function utilising 
    IBM's Watson AI NLP library. The function will call to the IBM service via the URL
    and process the response. There is also an error handling function for blank text.
"""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """ Decorator for flask app emotion detector function to route application calls.
        The submited text is passed to the URL and the generated response should be a
        dictionary that is parsed. Error handling included for blank text.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Generate the formatted response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Error handling for blank text
    if  dominant_emotion is None:
        return "Invalid text! Please try again."

    # Return the response
    detector_response = f"""For the given statement, the system response is 'anger': {anger_score},
    'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, 'sadness': {sadness_score}.
    The dominant emotion is {dominant_emotion}."""

    return detector_response


@app.route("/")
def render_index_page():
    """ Decorator for flask app root directory to route application calls
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
