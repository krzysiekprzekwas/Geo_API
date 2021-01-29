from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from app.config import postgresqlConfig
from app.resources.geo_data_resource import GeoData, GeoDataList
from app.resources.user import UserRegister
from app.security import authenticate, identity

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'What_do_You_think?'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(GeoData, '/geodata/<string:adress>')
api.add_resource(GeoDataList, '/geodata')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)

