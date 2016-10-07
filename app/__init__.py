# Import flask
from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)


# HTTP error handling
@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from app.components.twitter.controllers import twitterComponent

# Register blueprint(s)
app.register_blueprint(twitterComponent)
