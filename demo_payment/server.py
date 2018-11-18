""" Demo Payment Web Server """
import logging
from flask import Flask, session, redirect, url_for
from flask import escape, request, render_template
import os

app = Flask(__name__)


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.urandom(16)  # b'_5#y2L"F4Q8z\n\xec]/'


users = ['millerbott@gmail.com', 'jmb2341@columbia.edu']


@app.route("/")
def index(name=None):
    if 'email' in session:
        return render_template('index.html', name=escape(session['email']))
    return render_template('index.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login(message=None):
    if request.method == 'POST':
        session['email'] = request.form['email']
        if session['email'] in users:
            app.logger.info('%s logged in successfully', session['email'])
            return redirect(url_for('index'))
        else:
            app.logger.info('%s failed to log in', session['email'])
            return render_template('login.html',
                                   message='Email Not Registered')
    return render_template('login.html', message=None)


@app.route('/logout')
def logout():
    print("Logging Out")
    # remove the email from the session if it's there
    session.pop('email', None)
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):

    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)
