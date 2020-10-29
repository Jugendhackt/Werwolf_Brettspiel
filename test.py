install_requires=['flask', 'wrapt_timeout_decorator'
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return render_template("base.html")
