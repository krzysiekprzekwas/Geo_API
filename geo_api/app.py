from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from geo_api.config import postgresqlConfig
from geo_api.resources.geo_data_resource import GeoData, GeoDataList
from geo_api.resources.user import UserRegister
from geo_api.security import authenticate, identity

from geo_api.db import db

app = Flask(__name__)

app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'What_do_You_think?'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

db.init_app(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(GeoData, '/geodata/<string:address>')
api.add_resource(GeoDataList, '/geodata')
api.add_resource(UserRegister, '/register')

@app.route('/')
def index():
    return {'message': "Api interface only."}, 200


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
