from classifier import Classifier
from handlemail import MailHandler
from flask import Flask, redirect, url_for, request, render_template
import json

app = Flask(__name__)
clf = Classifier()
mail_handler = MailHandler(app)

@app.route("/", methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route("/debunk", methods=['GET', 'POST'])
def debunkpage():
    if request.method == 'POST':
        message_type = request.get_json(force=True)['messageType']

        if(message_type == "1"):
            article_text = request.get_json(force=True)['articleText']
            pred = clf.get_probabilities(article_text)
            diff = abs(pred[0][0] * 100 - (pred[0][1] * 100))
            conclusion = ''
            state = None

            if diff < 15: # determining how severe the difference in probability is
                conclusion = "We're on the fence :/"
                state = 1
            elif pred[0][0] > pred[0][1]:
                conclusion = "Hmmm... debunkd! :("
                state = 2
            else:
                conclusion = "Seems legit :)"
                state = 3

            response = { # constructing response
                'fakeProba': pred[0][0] * 100,
                'realProba': pred[0][1] * 100,
                'conclusion': conclusion,
                'state': state
            }
            return json.dumps(response) # returning json response for success function

    return render_template('debunk.html', prev_text ="")

@app.route("/about", methods=['GET'])
def aboutpage():
    return render_template('about.html')

@app.route("/contact", methods=['GET', 'POST'])
def contactpage():
    if request.method == "POST":
        email = request.get_json(force=True)['email']
        name = request.get_json(force=True)['name']
        subject = request.get_json(force=True)['subject']
        message = request.get_json(force=True)['message']

        mail_handler.send_message(app, name, email, subject, message) # sending email

    return render_template('contact.html')

def main():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()