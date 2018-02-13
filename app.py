from flask import Flask
from flask_restful import Api

from settings import (
    SERVER_SECRET_KEY
)

from resources.user import UserResource

app = Flask(__name__)
app.secret_key = SERVER_SECRET_KEY
api = Api(app)

api.add_resource(UserResource, '/user/<string:name>')

if __name__ == '__main__':
    app.run(port=5000)
