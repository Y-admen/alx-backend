# i18n
## Flask-Babel
It has builtin support for date formatting with timezone support as well as a very simple and friendly interface to **gettext translations**
ex
```python
from flask import Flask, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

translations = {
    'en': {'greeting': 'Hello, World!'},
    'es': {'greeting': '¡Hola, Mundo!'}
}

@app.route('/<lang>')
def index(lang):
    greeting = translations.get(lang, translations['en'])['greeting']
    return render_template('index.html', greeting=greeting)
```
## Translating steps
### 1-Inferring Locale
#### 1: Inferring Locale from URL Parameters
```python
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
" decorator isused to define a function that determines the best match for the user’s preferred langage"
def get_locale():
    return request.args.get('lang') or 'en'

translations = {
    'en': {'greeting': 'Hello, World!'},
    'es': {'greeting': '¡Hola, Mundo!'}
}
@app.route('/')
def index():
    lang = get_locale()
    greeting = translations.get(lang, translations['en'])['greeting']
    return render_template('index.html', greeting=greeting)
```

#### 2: Inferring Locale from User Settings (Stored in Session)
```python
from flask import Flask, request, render_template, session
from flask_babel import Babel

app = Flask(__name__)
app.secret_key = 'supersecretkey'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return session.get('lang', 'en')

translations = {
    'en': {'greeting': 'Hello, World!'},
    'es': {'greeting': '¡Hola, Mundo!'}
}

@app.route('/set_language/<lang>')
def set_language(lang):
    session['lang'] = lang
    return f'Language set to {lang}'

@app.route('/')
def index():
    lang = get_locale()
    greeting = translations.get(lang, translations['en'])['greeting']
    return render_template('index.html', greeting=greeting)
```

#### 3: Inferring Locale from Request Headers
```python
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'es'])

```
### 2-Marking Texts to Translate in Python Source Code
using **gettext()** method or **_**
```python
@app.route('/')
def index():
    greeting = gettext('Hello, World!')
    return render_template('index.html', greeting=greeting)
```
### 3-Marking Texts to Translate in Templates
Use the gettext function (aliased as _) in your Jinja2 templates to mark texts for translation.

```HTML

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ _('Hello, World!') }}</title>
</head>
<body>
    <h1>{{ greeting }}</h1>
</body>
</html>
```
### 4-Creating a Configuration File
Create a configuration file (babel.cfg) to instruct pybabel on which files to scan for translatable texts.

*[python: **.py]*
*[jinja2: templates/**.html]*


### 5-Extracting Text to Translate
Run the extraction command to generate the .pot file.
```bash
pybabel extract -F babel.cfg -k _l -o messages.pot .

```
### 6-Generating a Language Catalog
To create a translation catalog for a specific language, use the pybabel init command.

```bash
pybabel init -i messages.pot -d translations -l es
```
### 7-Editing the .po File
Edit the .po file to add translations.

Example of messages.po:


*msgid ""*
*msgstr ""*
*"Content-Type: text/plain; charset=UTF-8\n"*
*"Language: es\n"*

*#: app.py:12*
*msgid "Hello, World!"*
*msgstr "¡Hola, Mundo!"*

### 8-Compiling Translations
Compile the translations into a binary format (.mo file).

```bash
pybabel compile -d translations
```
Output:

The .mo files are used by the application during runtime for efficient translation retrieval.

### 9-Using Translations
Change your browser’s language settings to Spanish or modify the get_locale() function in the application to always return es to view translated texts.

Modified get_locale() function:

```Python

@babel.localeselector
def get_locale():
    return 'es'
```
### localize timestamps
##### pytz:  library allows accurate and cross platform timezone calculations
