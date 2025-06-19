#!/usr/bin/env python3
''' Flask app '''

<<<<<<< HEAD
from flask import Flask, render_template # type: ignore
=======
from flask import Flask, render_template

# type: ignore
>>>>>>> 889e9ff88310d6b330ededc779a5963988b16478
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    ''' return the template '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
