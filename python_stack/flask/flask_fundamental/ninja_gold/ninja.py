from flask import Flask, render_template, session, redirect, request 
app = Flask(__name__)
app.secret_key = 'keep it secrte'
import random
@app.route('/')
def index():
    if 'gold' in session:
        pass
    else:
        session['gold'] = 0

    return render_template('ninja.html', gold = session['gold']  )

@app.route('/process_money', methods = ['POST'])
def process_money():
    gold_activities = { 'farm':random.randint(10,20),
                        'cave': random.randint(5,10),
                        'house' : random.randint(2,5),
                        'casino': random.uniform(-50,50)}
    trial = request.form['building']
    if trial in ('farm', 'cave', 'house'):
        session['gold'] += gold_activities[trial]
    else:
        session['gold'] += int(gold_activities['casino'])
    return redirect('/')
app.run(debug= True)