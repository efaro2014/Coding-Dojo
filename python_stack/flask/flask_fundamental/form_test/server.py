from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret '
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print('*' * 50)
    print(request.form['name'])
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')
    # return render_template('show.html', name= name, email= email)

@app.route('/show')
def show_user():
    return render_template('show.html', name= session['name'], email= session['email'])

if __name__ == "__main__":
    app.run(debug=True)