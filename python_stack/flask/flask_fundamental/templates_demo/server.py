from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
    # return "hello world"

@app.route("/")
def index():
    infoDict = {
        "first_name": "Edward",
        "last_name": "Im",
        "friend_name" : "Steve",
        "num_friends": 5,
        "password" : "password",
        "list_of_friends" : ['zach', 'pramilla', 'irene']
    }
    return render_template('index.html', context = infoDict)

@app.route("/say/<name>/<num>")
def repeater(name, num):
    context = {
        "number":int(num),
        "name":name
    }
    return render_template('name.html', context = context)

if __name__ == "__main__":
    app.run(debug=True)