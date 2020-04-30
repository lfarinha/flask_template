from flask import Flask
from flask_restful import Api
from home_api import home

app = Flask(__name__)
Api(app)

app.register_blueprint(home, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
