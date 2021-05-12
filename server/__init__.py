from flask import Flask
print(__name__);
app = Flask(__name__.split('.')[0]);

@app.route('/')
def hello_world():
    return "hello world"

