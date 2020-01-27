from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        
        confession = request.form.get("confession")

        return render_template('success.html', confession=confession)

@app.route('/read')
def read():
    return render_template('read.html')