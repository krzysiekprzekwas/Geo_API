from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from geo_api.models.geo_data_model import GeoDataModel
from geo_api.build_geo_data import build_geo_data

class GeoData(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('adress', type=str, required=True, help='This field cannot be left blank')

    @jwt_required()
    def get(self, adress):
        item = GeoDataModel.find_by_adress(adress)
        if item:
            return item.json()
        return {'message': 'GeoData not found'}, 404

    @jwt_required()
    def post(self, adress):
        item = GeoDataModel.find_by_adress(adress)
        if item:
            return {'message': f"GeoData with this adress '{adress}' already exists."}, 400

        data = GeoData.parser.parse_args()

        if data['adress'] is not adress:
            return {'message': f"Different adress in url and in body. {adress} vs {data["adress"]}"}, 400
        
        try:
            item = build_geo_data(adress)
            item.save_to_db()
        except:
            return {"message": "An error occurred while inserting the GeoData."}, 500
        return item.json(), 201

    @jwt_required()
    def delete(self, adress):
        item = GeoDataModel.find_by_adress(adress)
        if item:
            item.delete_from_db()

            return {'message': 'GeoData has been deleted'}

    @jwt_required()
    def put(self, adress):
        data = GeoData.parser.parse_args()
        item = GeoDataModel.find_by_adress(adress)

        try:
            if item is None:
                item = build_geo_data(adress)
            else:
                item.adress = data['adress']
    
            item.save_to_db()
        except:
            return {"message": "An error occurred while updating the GeoData."}, 500

        return item.json()

class GeoDataList(Resource):
    
    @jwt_required()
    def get(self):
        return {'geoDates': [geodata.json() for geodata in GeoDataModel.query.all()]}
        