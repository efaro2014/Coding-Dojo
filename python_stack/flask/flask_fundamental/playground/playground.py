from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('ground.html', times = 3, color = 'blue')

@app.route('/play/<times>')
def ground(times):
    times = int(times)
    return render_template('ground.html', times=times, color= 'blue')


@app.route('/play/<times>/<color>')
def different(times, color):
    times = int(times)
    return render_template('ground.html', times=times,
     color= color)
if __name__ == '__main__':
    app.run(debug =True) 