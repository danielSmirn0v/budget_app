
from budget_app import app

from flask import Flask, render_template, request, redirect, session, flash

from budget_app.models import users

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('test.html')