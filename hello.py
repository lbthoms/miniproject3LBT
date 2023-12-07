# INF601 - Advanced Programming in Python
# Lisa Thoms
# Mini Project 3


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'