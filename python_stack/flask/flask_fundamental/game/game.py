from flask import Flask 
app = Flask(__name__)
@app.route('/')
def hello():
    return "Welcome to the park, where do you wanna go Left or Right!"
@app.route('/left')
def left():
    return "Welcome to the zoo, what do you wanna see Tiger or Monkey"
@app.route('/left/tiger')
def tiger():
    return "Oh no, you will be eaten by tiger"

@app.route('/left/monkey')
def monkey():
    return "Oh no, the monkey is hungry give him banana"
@app.route('/right')
def right():
    return "Oh no you are in the hell, but don't worry you have options just pick a number from b/n 1 and 5"

@app.route('/right/<num>')
def number(num):
    num = int(num)
    if num == 3:
        return 'oh OMG, you escaped, good job Prammila'
    if num < 3:
        return 'oh poor Pramilla you will be eaten by a monster'
    else:
        return 'wait for a rescue to come'
app.run(debug=True)