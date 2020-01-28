from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        confession = request.form.get("confession")
        return render_template('success.html', confession=confession)

@app.route('/read')
def read():
    
    if request.method == 'GET':
        return render_template('read.html')
    
    elif request.method == 'POST':
        return render_template('view.html', secret="secret")