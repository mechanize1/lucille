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

from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    # Containers to hold description and photos
    desc = []
    photo = []
    return 'Hello world!'

if __name__ == '__main__':
    main()
