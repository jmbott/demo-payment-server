""" Demo Payment Web Server """
import logging
from flask import Flask
from flask import render_template
app = Flask(__name__)

from demo_payment import options


@app.route("/")
def hello():
    return "Hello World!"
#def get():
#    return render_template('base.html')


def main():
    print('Listening on port 8888')
    app.run(host='127.0.0.1', port=8888, debug=True)
    logging.info('Application started')


if __name__ == '__main__':
    main()
