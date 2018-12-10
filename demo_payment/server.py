"""Demo Payment Web Server."""

from flask import Flask, session, redirect, url_for
from flask import escape, request, render_template
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
# from demo_payment.options import options
from demo_payment import models
import os
import stripe

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.urandom(16)  # b'_5#y2L"F4Q8z\n\xec]/'

user_list = ['millerbott@gmail.com', 'jmb2341@columbia.edu']

def create_session():
    """Create a Session."""
    engine = models.create_engine()
    sesh = sessionmaker(bind=engine)()
    return sesh


def get_api_key():
    """Get stripe api_key in DB."""
    if 'sesh' not in locals() and 'sesh' not in globals():
        sesh = create_session()
    Str = models.Stripe
    keys = sesh.query(Str).order_by(Str.key)
    for key in keys:
        stripe_key = key.api_key
    return stripe_key


def add_api_key(key):
    """Add a new Stripe api_key to the DB.
    See your keys here: https://dashboard.stripe.com/account/apikeys"""
    try:
        if 'sesh' not in locals() and 'sesh' not in globals():
            sesh = create_session()
        with models.transaction(sesh) as sesh:
            sesh.add(models.Stripe(api_key=key))
        message = f'{key[:6]}... successfully added'
    except IntegrityError as error:
        message = f'{error}'
    return message


def get_users():
    """Get all users in DB."""
    if 'sesh' not in locals() and 'sesh' not in globals():
        sesh = create_session()
    user_list = []
    users = sesh.query(models.User).order_by('email')
    for user in users:
        user_list.append(user.email)
    return user_list


def add_user(email):
    """Add a new User to the DB."""
    try:
        if 'sesh' not in locals() and 'sesh' not in globals():
            sesh = create_session()
        with models.transaction(sesh) as sesh:
            sesh.add(models.User(email=email))
        message = f'{email} successfully added'
    except IntegrityError as error:
        if 'user_email_check' in error.orig.pgerror:
            message = f'{email} is not a valid e-mail address'
        else:
            message = f'Account for {email} already exists'
    return message


@app.route("/")
def index(name=None):
    """Route Index."""
    if 'email' in session:
        return render_template('index.html', name=escape(session['email']))
    return render_template('index.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login(message=None):
    """Login Route."""
    if request.method == 'POST':
        session['email'] = request.form['email']
        if session['email'] in user_list:
            app.logger.info('%s logged in successfully', session['email'])
            return redirect(url_for('index'))
        else:
            app.logger.info('%s failed to log in', session['email'])
            return render_template('login.html',
                                   message='Email Not Registered')
    return render_template('login.html', message=None)


@app.route('/logout')
def logout():
    """Logout Route."""
    print("Logging Out")
    # remove the email from the session if it's there
    session.pop('email', None)
    return redirect(url_for('index'))


@app.route('/stripe_demo', methods=['GET', 'POST'])
def stripe_demo(message=None):
    """Stripe Route."""
    if 'email' in session:
        if request.method == 'POST':
            stripe.api_key = get_api_key()
            # Token is created using Checkout or Elements!
            # Get the payment token ID submitted by the form:
            token = request.form['stripeToken']
            print(token)
            charge = stripe.Charge.create(
                amount=999,
                currency='usd',
                description='Example charge',
                source=token,
            )
            return render_template('stripe_demo.html', message=charge)
        return render_template('stripe_demo.html', message=None)
    return redirect(url_for('login'))


@app.route('/twilio')
def twilio():
    """Twilio Route."""
    if 'email' in session:
        return render_template('twilio.html', name=escape(session['email']))
    return redirect(url_for('login'))


@app.errorhandler(404)
def not_found(error):
    """Error 404."""
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)
