#!/usr/bin/env python3
"""Get locale and timezone from request"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
import pytz.exceptions

app = Flask(__name__)


class Config:
    """Class to set Babel's default locale and available languages"""

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
    """Returns a user dictionary or None"""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """Find a user if any, and set it as a global on g.user"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages"""
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    if g.user and g.user['locale'] and \
            g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Determine the best match with our supported time zones"""
    # Timezone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Timezone from user settings
    if g.user and g.user['timezone']:
        try:
            return pytz.timezone(g.user['timezone'])
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Default timezone
    return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


@app.route('/')
def render_temp():
    """Create a single / route and an index.html"""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run()
