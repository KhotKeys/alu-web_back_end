#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)

# Fake translations for testing
translations = {
    'en': {
        'home_title': 'Welcome to Holberton',
        'home_header': 'Hello world!',
    },
    'fr': {
        'home_title': 'Bienvenue chez Holberton',
        'home_header': 'Bonjour monde!',
    }
}


@app.context_processor
def inject_gettext():
    """Inject a fake gettext _ function for templates"""
    def fake_gettext(key):
        lang = get_locale()
        return translations.get(lang, {}).get(key, key)
    return dict(_=fake_gettext)


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'])
def hello():
    """ GET /
    Return:
      - Render template
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
