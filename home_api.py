from flask import Blueprint
from flask_restful import Resource, Api

home = Blueprint('home', __name__)
api = Api(home)


class Home(Resource):
    def get(self):
        return "Fuck Yeah", 200


api.add_resource(Home, '/', methods=['GET'])
