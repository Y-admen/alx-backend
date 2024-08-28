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

### Inferring Locale
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
### Translating Text in Flask Applications
using **gettext()** method
```python
@app.route('/')
def index():
    greeting = gettext('Hello, World!')
    return render_template('index.html', greeting=greeting)
```
### localize timestamps
##### pytz:  library allows accurate and cross platform timezone calculations
