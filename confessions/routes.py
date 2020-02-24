from flask import Flask, render_template, request, session
from flask import current_app as app
from .models import db, Confession
from datetime import datetime

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        confession = request.form.get("confession")
        new_confession = Confession(confession=confession, created=datetime.now())
        db.session.add(new_confession)
        db.session.commit()
        return render_template('success.html', confessions=db.session.query(Confession).all())

@app.route('/read')
def read():
    
    if request.method == 'GET':
        return render_template('read.html')
    
    elif request.method == 'POST':
        return render_template('view.html', secret="secret")