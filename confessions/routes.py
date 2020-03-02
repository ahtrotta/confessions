from flask import Flask, render_template, request, session
from flask import current_app as app
from .models import Confession
from . import db
from datetime import datetime
from random import choice

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/confess', methods=['POST', 'GET'])
def confess():
    
    if request.method == 'GET':
        return render_template('confess.html')

    elif request.method == 'POST':
        confession = request.form.get("confession")
        new_confession = Confession(confession=confession, created=datetime.now())
        db.session.add(new_confession)
        db.session.commit()
        return render_template('success.html', confessions=db.session.query(Confession).all())

@app.route('/read', methods=['POST', 'GET'])
def read():
    
    if request.method == 'GET':
        return render_template('read.html')
    
    elif request.method == 'POST':
        ids = db.session.query(Confession.id).all()
        id_list = []
        for id, in ids:
            id_list.append(id)
        rand_id = choice(id_list)
        secret = db.session.query(Confession).filter(Confession.id == rand_id).all()
        db.session.delete(secret[0])
        db.session.commit()
        return render_template('view.html', secret=secret[0].confession)
