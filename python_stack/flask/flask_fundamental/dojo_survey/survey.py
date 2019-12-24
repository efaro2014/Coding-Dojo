from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = 'keep it secret '
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def create_user():
    print(request.form['name'])
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['language'] = request.form['language']
    session['description']= request.form['description']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html', name= session['name'], location= session['dojo_location'], langauge =  session['language'],
        description =  session['description'])

if __name__ == "__main__":
    app.run(debug=True)