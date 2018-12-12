"""Demo Payment Web Server."""

from flask import Flask, session, redirect, url_for
from flask import escape, request, render_template
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import desc
from demo_payment import models
from twilio.rest import Client
from twilio.base.exceptions import TwilioException
import os
import datetime
import stripe
from stripe.error import AuthenticationError

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.urandom(16)  # b'_5#y2L"F4Q8z\n\xec]/'


def create_session(ensure=True):
    """Create a Session."""
    engine = models.create_engine()
    if ensure:
        models.Base.metadata.create_all(engine)
        print(f'Created schema {models.Base.metadata.schema}')
    return sessionmaker(bind=engine)()


def get_api_key():
    """Get stripe api_key in DB."""
    if 'sesh' not in locals() and 'sesh' not in globals():
        sesh = create_session(ensure=False)
    Str = models.Stripe
    keys = sesh.query(Str).order_by(Str.ts)
    stripe_key = ''
    for key in keys:
        stripe_key = key.api_key
    return stripe_key


def add_api_key(key):
    """Add a new Stripe api_key to the DB."""
    try:
        if 'sesh' not in locals() and 'sesh' not in globals():
            sesh = create_session(ensure=False)
        data = {
            'ts': datetime.datetime.now().isoformat(),
            'api_key': key}
        statement = (
            insert(models.Stripe)
            .values(**data)
            .on_conflict_do_update(index_elements=['api_key'], set_=data))
        with models.transaction(sesh) as sesh:
            # See your keys here: https://dashboard.stripe.com/account/apikeys
            sesh.execute(statement)
        message = f'{key[:7]}... successfully added'
    except IntegrityError as error:
        message = f'{error}'
    return message


def get_twilio_info():
    """Get Twilio Info in DB."""
    if 'sesh' not in locals() and 'sesh' not in globals():
        sesh = create_session(ensure=False)
    Twi = models.Twilio
    info = sesh.query(Twi).order_by(desc(Twi.ts))
    twilio_info = []
    for inf in info:
        twilio_info.append(inf.account_sid)
        twilio_info.append(inf.auth_token)
        twilio_info.append(inf.dest_num)
        twilio_info.append(inf.orig_num)
    return twilio_info


def add_twilio_info(sid, token, dest, orig):
    """Add new Twilio info to the DB."""
    try:
        if 'sesh' not in locals() and 'sesh' not in globals():
            sesh = create_session(ensure=False)
        data = {
            'ts': datetime.datetime.now().isoformat(),
            'account_sid': sid,
            'auth_token': token,
            'dest_num': dest,
            'orig_num': orig}
        statement = (
            insert(models.Twilio)
            .values(**data)
            .on_conflict_do_update(index_elements=['account_sid'], set_=data))
        with models.transaction(sesh) as sesh:
            # Your Account SID and Auth Token from twilio.com/console
            sesh.execute(statement)
        message = \
            f'{sid[:6]}..., {token[:6]}..., {dest}, {orig} successfully added'
    except IntegrityError as error:
        message = f'error: {error}'
    return message


def get_users():
    """Get all users in DB."""
    if 'sesh' not in locals() and 'sesh' not in globals():
        sesh = create_session(ensure=False)
    user_list = []
    users = sesh.query(models.User).order_by('email')
    for user in users:
        user_list.append(user.email)
    return user_list


def add_user(email):
    """Add a new User to the DB."""
    try:
        if 'sesh' not in locals() and 'sesh' not in globals():
            sesh = create_session(ensure=False)
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
        user_list = get_users()
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
            try:
                stripe.api_key = get_api_key()
                # Token is created using Checkout or Elements!
                # Get the payment token ID submitted by the form:
                token = request.form['stripeToken']
                charge = stripe.Charge.create(
                    amount=999,
                    currency='usd',
                    description='Example charge',
                    source=token,
                )
            except AuthenticationError as error:
                charge = f'error: {error}'
            return render_template('stripe_demo.html', message=charge)
        return render_template('stripe_demo.html', message=None)
    return redirect(url_for('login'))


@app.route('/twilio_demo', methods=['GET', 'POST'])
def twilio_demo(message=None):
    """Twilio Route."""
    if 'email' in session:
        if request.method == 'POST':
            try:
                info = get_twilio_info()
                account_sid = info[0]
                auth_token = info[1]
                client = Client(account_sid, auth_token)
                print(client)
                mess = request.form['twilioMessage']
                print(mess)
                message_send = client.messages.create(
                    to=info[2],
                    from_=info[3],
                    body=mess)
            except IndexError:
                message_send = f'error: twilio info not set'
            except TwilioException:
                message_send = f'error: invalid twilio details'
            return render_template('twilio_demo.html', message=message_send)
        return render_template('twilio_demo.html', message=None)
    return redirect(url_for('login'))


@app.route('/settings', methods=['GET', 'POST'])
def settings(message=None): # noqa
    """Settings Route."""
    if 'email' in session:
        if request.method == 'POST':
            if request.form['btn'] == 'Add User':
                email = request.form['addUser']
                message = add_user(email)
            elif request.form['btn'] == 'Add Stripe Info':
                key = request.form['addStripeKey']
                message = add_api_key(key)
            elif request.form['btn'] == 'Add Twilio Info':
                sid = request.form['addTwilioSID']
                token = request.form['addTwilioToken']
                dest = request.form['addTwilioDest']
                orig = request.form['addTwilioOrig']
                message = add_twilio_info(sid, token, dest, orig)
            return render_template('settings.html', message=message)
        return render_template('settings.html', message=None)
    return redirect(url_for('login'))


@app.errorhandler(404)
def not_found(error):
    """Error 404."""
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)
