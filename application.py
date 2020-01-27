from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        return render_template('success.html')

@app.route('/read')
def read():
    return render_template('read.html')