#!flask/bin/python
from gevent import monkey

monkey.patch_all()  # for making server non-blocking, flask is by defualt blocking
from gevent import wsgi
import config
from werkzeug.serving import run_with_reloader
from werkzeug.debug import DebuggedApplication
from app import app

"""

	API Response Struct In Success:
	{
		success: true,
		data: {}
	}

	API Response Struct In Error:
	{
		success: true,
		error: {
			message: "some string",
			code: some int num
		}
	}
"""


@run_with_reloader
def runServer():
	server = wsgi.WSGIServer((config.HOST, config.PORT),
							 DebuggedApplication(app))  # passing flask app(in debug mode) var in WSGI server by gevent
	server.serve_forever()


if __name__ == '__main__':
	runServer()  # starting the server here
