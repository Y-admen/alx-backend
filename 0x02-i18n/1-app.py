#!/usr/bin/env python
"Basic Babel setup"
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    "class to set Babel's default locale and available languages"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def render_temp():
    """Create a single / route and an index.html

    Returns:
        templates to render
    """
    return render_template("1-index.html")


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
