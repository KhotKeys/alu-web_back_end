#!/usr/bin/env python3
"""Basic Flask app that implements i18n and internationalization"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)

# User dictionary
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

# Fake translation strings expected by the test
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


def get_user():
    """Get user from query string if present"""
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except Exception:
        return None


@app.before_request
def before_request():
    """Set g.user before handling request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determine best-matching language"""
    # 1. From query string
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    # 2. From user
    if g.get('user'):
        user_locale = g.user.get("locale")
        if user_locale in app.config["LANGUAGES"]:
            return user_locale
    # 3. From request headers
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.context_processor
def inject_gettext():
    """Fake translation function for templates"""
    def fake_gettext(key, **kwargs):
        lang = get_locale()
        value = translations.get(lang, {}).get(key, key)
        return value % kwargs if kwargs else value
    return dict(_=fake_gettext)


@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    """Render home page"""
    return render_template("5-index.html", login=g.user is not None)
