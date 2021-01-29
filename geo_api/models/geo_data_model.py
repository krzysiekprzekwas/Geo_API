from geo_api.db import db


class GeoDataModel(db.Model):
    __tablename__ = 'geodates'

    id = db.Column(db.Integer, primary_key=True)
    adress = db.Column(db.String(80))
    adress_type = db.Column(db.String(4))
    continent_name = db.Column(db.String(80))
    country_name = db.Column(db.String(80))
    region_name = db.Column(db.String(80))

    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())

    def __init__(self, adress, adress_type, continent_name, country_name, region_name, latitude, longitude):
        self.adress =adress
        self.adress_type=adress_type
        self.continent_name=continent_name
        self.country_name=country_name
        self.region_name=region_name
        self.latitude=latitude
        self.longitude=longitude

    def json(self):
        return {
            'id'            : self.id, 
            'adress'        : self.adress,
            'adress_type'   : self.adress_type,
            'continent_name': self.continent_name,
            'country_name'  : self.country_name,
            'region_name'   : self.region_name,
            'latitude'      : self.latitude,
            'longitude'     : self.longitude
            }

    @classmethod
    def find_by_adress(cls, adress):
        return cls.query.filter_by(adress=adress).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit() 

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
