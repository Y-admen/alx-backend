#!/usr/bin/env python
"Basic Babel setup"
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

class Config:
    "class to set Babel's default locale and available languages"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

@app.route("/")
def render_temp():
    """Create a single / route and an index.html

    Returns:
        templates to render 
    """
    greeting1 = "Welcome to Holberton"
    greeting2 = "Hello world"
    return render_template('1-index.html', greeting1=greeting1, greeting2=greeting2)
