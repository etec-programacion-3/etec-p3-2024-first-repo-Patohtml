from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "hello word"

@app.route("/byebye")
def byebye():
    return "goodbye"

app.run()