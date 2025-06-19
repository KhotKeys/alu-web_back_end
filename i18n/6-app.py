#!/usr/bin/env python3
"""Basic Flask app that implements i18n and internationalization"""

from flask import Flask, render_template, request, g
<<<<<<< HEAD
from flask_babel import Babel
=======
>>>>>>> 889e9ff88310d6b330ededc779a5963988b16478

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
<<<<<<< HEAD
    """Config class for your application, it deals with babel mostly"""
=======
    """Config class for your application, it deals with i18n"""
>>>>>>> 889e9ff88310d6b330ededc779a5963988b16478
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
<<<<<<< HEAD
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale for your application"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    user = g.get('user')
    if (user and user.get("locale", None)
            and user["locale"] in app.config['LANGUAGES']):
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Home page for your application"""
    login = False
    if g.get('user'):
        login = True
    return render_template('6-index.html', login=login)


def get_user():
    """Get user information from users dict"""
    try:
        login_as = int(request.args.get('login_as'))
        return users.get(int(login_as))
=======

# Fake translation data for test
translations = {
    'en': {
        'home_title': 'Welcome to Holberton',
        'home_header': 'Hello world!',
        'logged_in_as': 'You are logged in as %(username)s.',
        'not_logged_in': 'You are not logged in.',
    },
    'fr': {
        'home_title': 'Bienvenue chez Holberton',
        'home_header': 'Bonjour monde!',
        'logged_in_as': 'Vous êtes connecté en tant que %(username)s.',
        'not_logged_in': 'Vous n\'êtes pas connecté.',
    }
}


def get_locale():
    """Get best match language"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    user = g.get('user')
    if user:
        user_locale = user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    return 'en'


@app.context_processor
def inject_gettext():
    """Injects a fake translation function into the template context"""
    def fake_gettext(key, **kwargs):
        lang = get_locale()
        value = translations.get(lang, {}).get(key, key)
        return value % kwargs if kwargs else value
    return dict(_=fake_gettext)


def get_user():
    """Get user from request"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
>>>>>>> 889e9ff88310d6b330ededc779a5963988b16478
    except Exception:
        return None


@app.before_request
def before_request():
<<<<<<< HEAD
    """Before request"""
    user = get_user()
    print(user)
    if user:
        g.user = user
=======
    """Before request to set user"""
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Render the homepage"""
    return render_template('6-index.html', login=g.user is not None)
>>>>>>> 889e9ff88310d6b330ededc779a5963988b16478


if __name__ == "__main__":
    app.run()
