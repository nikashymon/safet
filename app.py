from flask import Flask, render_template, request, session, redirect, flash
import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask('test website')
app.secret_key = os.urandom(24)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()