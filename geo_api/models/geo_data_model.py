from geo_api.db import db


class GeoDataModel(db.Model):
    __tablename__ = 'geodates'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(80))
    address_type = db.Column(db.String(4))
    continent_name = db.Column(db.String(80))
    country_name = db.Column(db.String(80))
    region_name = db.Column(db.String(80))

    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())

    def __init__(self, address, address_type, continent_name, country_name, region_name, latitude, longitude):
        self.address =address
        self.address_type=address_type
        self.continent_name=continent_name
        self.country_name=country_name
        self.region_name=region_name
        self.latitude=latitude
        self.longitude=longitude

    def json(self):
        return {
            'id'            : self.id, 
            'address'        : self.address,
            'address_type'   : self.address_type,
            'continent_name': self.continent_name,
            'country_name'  : self.country_name,
            'region_name'   : self.region_name,
            'latitude'      : self.latitude,
            'longitude'     : self.longitude
            }

    @classmethod
    def find_by_address(cls, address):
        return cls.query.filter_by(address=address).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit() 

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
