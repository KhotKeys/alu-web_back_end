#!/usr/bin/env python3
"""Basic Flask app that implements i18n and internationalization"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class for your application, it deals with babel mostly"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


# Fake translation data
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


@babel.localeselector
def get_locale():
    """Get locale for your application"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    user = g.get('user')
    if user and user.get("locale") in app.config['LANGUAGES']:
        return user.get("locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.context_processor
def inject_gettext():
    """Inject a fake _ function for template translation"""
    def fake_gettext(key, **kwargs):
        lang = get_locale()
        value = translations.get(lang, {}).get(key, key)
        return value % kwargs if kwargs else value
    return dict(_=fake_gettext)


def get_user():
    """Get user information from users dict"""
    try:
        login_as = int(request.args.get('login_as'))
        return users.get(int(login_as))
    except Exception:
        return None


@app.before_request
def before_request():
    """Before request"""
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Home page for your application"""
    return render_template('5-index.html', login=g.user is not None)


if __name__ == "__main__":
    app.run()
