#!/usr/bin/env python3
"Get locale from request"
from flask import Flask, render_template, request
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
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
