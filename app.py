"""
__author__ = "Sylvestor George"
__version__ = "1.0"
__maintainer__ = "Sylvestor George"
__email__ = "sylvestor.george88@gmail.com"
"""
# System/Library Imports
import os
from flask import Flask
from flask import jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Custom Imports
from handlers.events import events
from handlers.engineers import engineers

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    """
    Slack Technical Challenge Services
    """
    return make_response(jsonify(message='Slack Technical Challenge Services are Running'),
                         200)


app.register_blueprint(events, url_prefix='/events')
app.register_blueprint(engineers, url_prefix='/engineers')

if __name__ == '__main__':
    app.debug = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(host='0.0.0.0', port=8888)
