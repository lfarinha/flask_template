from flask import Blueprint
from flask_restful import Resource, Api

gato = Blueprint('gato', __name__)
api = Api(gato)


class Gato(Resource):
    def __init__(self):
        self.gato = 'el gato lo mama rico'

    def get(self):
        return self.gato, 200


api.add_resource(Gato, '/', methods=['GET'])
