#!/usr/bin/env python3
"Get locale from request"
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)


class Config:
    "class to set Babel's default locale and available languages"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    "returns a user dictionary or None"
    user = request.args.get('login_as')
    if user and user in users:
        return user
    return None


@app.befor_request
def before_request():
    " find a user if any, and set it as a global on g.user"
    g.user = get_user()


@app.route('/')
def render_temp():
    """Create a single / route and an index.html"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
