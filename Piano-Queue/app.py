from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! It\'s-a me, Mario! Let\'s-a go!'