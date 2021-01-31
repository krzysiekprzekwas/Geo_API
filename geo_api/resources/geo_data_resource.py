from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from geo_api.models.geo_data_model import GeoDataModel


class GeoData(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('address', type=str, required=True, help='This field cannot be left blank')

    @jwt_required()
    def get(self, address):
        item = GeoDataModel.find_by_address(address)
        if item:
            return item.json()
        return {'message': 'GeoData not found'}, 404

    @jwt_required()
    def post(self, address):
        item = GeoDataModel.find_by_address(address)
        if item:
            return {'message': f"GeoData with this address '{address}' already exists."}, 400

        data = GeoData.parser.parse_args()

        if data['address'] is not address:
            return {'message': "Different address in url and in body. {} vs {}".format(address, data[
                "address"])}, 400

        try:
            item = build_geo_data(address)
            item.save_to_db()
        except:
            return {"message": "An error occurred while inserting the GeoData."}, 500
        return item.json(), 201

    @jwt_required()
    def delete(self, address):
        item = GeoDataModel.find_by_address(address)
        if item:
            item.delete_from_db()

            return {'message': 'GeoData has been deleted'}

    @jwt_required()
    def put(self, address):
        data = GeoData.parser.parse_args()
        item = GeoDataModel.find_by_address(address)

        try:
            if item is None:
                item = build_geo_data(address)
            else:
                item.address = data['address']

            item.save_to_db()
        except:
            return {"message": "An error occurred while updating the GeoData."}, 500

        return item.json()


class GeoDataList(Resource):

    @jwt_required()
    def get(self):
        return {'geoDates': [geodata.json() for geodata in GeoDataModel.query.all()]}
