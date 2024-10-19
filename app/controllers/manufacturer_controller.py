from app import db
from app.models.manufacturer import Manufacturer


class ManufacturerController:
    @staticmethod
    def get_all_manufacturers():
        return Manufacturer.query.all()

    @staticmethod
    def get_manufacturer_by_id(manufacturer_id):
        return Manufacturer.query.get(manufacturer_id)

    @staticmethod
    def add_manufacturer(name, description, country, certificates, internal_id):
        manufacturer = Manufacturer(name=name, description=description, country=country, 
                                    certificates=certificates, internal_id=internal_id)
        db.session.add(manufacturer)
        db.session.commit()
