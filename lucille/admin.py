"""
Customer-facing services that listens for incoming service requests from tenets.  Messages come in two forms:

Message system
    1.  General inquiries sent to our email
Ticket system
    1.  Specific inquiries with the problem
        - We provide a menu of choices:  toilet, tub, sink, etc.
        - The user snaps a photo, and leaves a description of the issue
        - We respond with acknowledgment and 24-hour notice.
Methodology:
    - Poll for incoming connections from tenet

"""
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
 
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'admin.db'),
    SECRET_KEY='secret-key',
    USERNAME='admin',
    PASSWORD='password'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

MAIL_USERNAME = 'user@user.cm'
MAIL_PASSWORD = 'password'
MAIL_DEFAULT_SENDER = "'Sender' <noreply@example.com>"
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect('schema.sql')
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.route('/issue/')
def issue(var='Brian'):
    return render_template('issue.html', name=var)

@app.route('/profile/')
def profile(var=None):
    return render_template('profile.html')

@app.route('/readings/')
def readings(var=None):
    return render_template('readings.html')

@app.route('/')
def main():
    # Containers to hold description and photos
    desc = []
    photo = []
    return 'Main page'

if __name__ == '__main__':
    main()
