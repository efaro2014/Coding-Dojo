from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def helloworld():
    return render_template('index.html')
@app.route('/success')
def success():
    return "Success!!"
# @app.route('/<name>/<age>')
# def hello(name, age):
#     return ('I am {} and am {} years old '.format(name, int(age)))

@app.route('/<name>/<times>')
def hello(name, times):
    return render_template('index.html', sname = name, stimes = int(times))

if __name__ == '__main__':
    app.run(debug =True) 