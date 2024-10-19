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
        
    @staticmethod
    def update_manufacturer(manufacturer, name, description, country, certificates, internal_id):
        manufacturer.name = name
        manufacturer.description = description
        manufacturer.country = country
        manufacturer.certificates = certificates
        manufacturer.internal_id = internal_id
        db.session.commit()

    @staticmethod
    def delete_manufacturer(manufacturer_id):
        manufacturer = ManufacturerController.get_manufacturer_by_id(manufacturer_id)
        if manufacturer:
            db.session.delete(manufacturer)
            db.session.commit()
            return True
        return False
