from flask import Flask, render_template
from flask_ask import Ask, question, session, statement
import logging
from random import randint

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@app.launch
def launcher():
    message = render_template('start')
    return question(message)

@app.intent("yesIntent")
def yes():
    message = render_template('yes')
    return question(message)

@app.intent('noIntent')
def no():
    message = render_template('no')
    return statement(message)

@app.intent('numberOfRollsIntent', convert = {'number': int})
def many_rolls(number):
    total = 0
    for i in range(number):
        total = total + randint(1,7)
    message = "Your total is {}".format(total)
    return statement(message)

@app.session_ended
def end():
    message = render_template('end')
    return statement(message)

if __name__ == "__main__":
    app.run(debug = True)
