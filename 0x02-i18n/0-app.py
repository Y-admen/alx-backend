#!/usr/bin/env python3
"Basic Flask app"
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def render_temp():
    """Create a single / route and an index.html

    Returns:
        templates to render 
    """
    greeting1 = "Welcome to Holberton"
    greeting2 = "Hello world"
    return render_template('0-index.html', greeting1=greeting1, greeting2=greeting2)

if __name__ == '__main__':
    app.run()
