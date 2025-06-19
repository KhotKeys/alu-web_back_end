#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

<<<<<<< HEAD
=======
app = Flask(__name__)
app.url_map.strict_slashes = False

>>>>>>> 889e9ff88310d6b330ededc779a5963988b16478

class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
<<<<<<< HEAD


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)

babel = Babel(app)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'
=======
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
>>>>>>> 889e9ff88310d6b330ededc779a5963988b16478


@app.route('/', methods=['GET'])
def hello():
    """ GET /
    Return:
      - Render template
    """
    return render_template('4-index.html')


<<<<<<< HEAD
@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


=======
>>>>>>> 889e9ff88310d6b330ededc779a5963988b16478
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
