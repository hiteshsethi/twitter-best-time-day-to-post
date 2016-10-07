# Import flask
from flask import Flask, send_from_directory

# Define the WSGI application object
app = Flask(__name__)


# HTTP error handling
@app.errorhandler(404)
def not_found(error):
	return send_from_directory("templates", "404.html"), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from app.components.twitter.controllers import twitterComponent

# Register blueprint(s)
app.register_blueprint(twitterComponent)
