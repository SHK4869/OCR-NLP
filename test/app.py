from flask import Flask, render_template, request, jsonify
import json
from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob
training_corpus = [
                   ('I am exhausted of this work.', 'Class_B'),
                   ("I can't cooperate with this", 'Class_B'),
                   ('He is my badest enemy!', 'Class_B'),
                   ('My management is poor.', 'Class_B'),
                   ('I love this burger.', 'Class_A'),
                   ('This is an brilliant place!', 'Class_A'),
                   ('I feel very good about these dates.', 'Class_A'),
                   ('This is my best work.', 'Class_A'),
                   ("What an awesome view", 'Class_A'),
                   ('I do not like this dish', 'Class_B')]
test_corpus = [
                ("I am not feeling well today.", 'Class_B'), 
                ("I feel brilliant!", 'Class_A'), 
                ('Gary is a friend of mine.', 'Class_A'), 
                ("I can't believe I'm doing this.", 'Class_B'), 
                ('The date was good.', 'Class_A'), ('I do not enjoy my job', 'Class_B')]

model = NBC(training_corpus) 

"""
import pyrebase
config = {
    "apiKey": "AIzaSyCH7jI33F36_lE81BqcEz9uu_joEr_6IqY",
    "authDomain": "flask-139b1.firebaseapp.com",
    "databaseURL": "https://flask-139b1.firebaseio.com",
    "projectId": "flask-139b1",
    "storageBucket": "",
    "messagingSenderId": "40854891066"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
#authenticate a user
all_agents = db.child("agents").get(user['idToken']).val()

"""

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods = ['GET','POST'])
def get():
    #idd= jsonify(request.json)
    print (request.is_json)
    content = request.get_json()
    print (content)
    print(model.classify(content['text']))

   
    return "Hello"

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug = True, port = 5000)