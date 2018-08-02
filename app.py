"""
__author__ = "Sylvestor George"
__version__ = "1.0"
__maintainer__ = "Sylvestor George"
__email__ = "sylvestor.george88@gmail.com"
"""
from flask import Flask
from flask import jsonify, make_response
from flask_cors import CORS
from flasgger import Swagger

from handlers.events import events
from handlers.engineers import engineers

# Initializing Flask application
application = Flask(__name__)
application.debug = True
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Cross Origin
CORS(application)

# Flask Swagger
swagger = Swagger(application)


@application.route('/', methods=['GET'])
def index():
    """
    Slack Technical Challenge Services
    """
    return make_response(jsonify(message='Slack Technical Challenge!'),
                         200)


# Registers Flask Blueprints
application.register_blueprint(events, url_prefix='/events')
application.register_blueprint(engineers, url_prefix='/engineers')

application.config['SWAGGER'] = {
    'title': 'DILS Flasgger RESTful',
    'uiversion': 3,
    'swagger_version': '2.0',

    'headers': [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS'),
        ('Access-Control-Allow-Credentials', 'true'),
    ]
}

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8888)
