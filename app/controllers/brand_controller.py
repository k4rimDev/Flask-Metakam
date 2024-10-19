from app import db
from app.models.brand import Brand


class BrandController:
    @staticmethod
    def get_all_brands():
        return Brand.query.all()

    @staticmethod
    def get_brand_by_id(brand_id):
        return Brand.query.get(brand_id)

    @staticmethod
    def add_brand(logo, name, description, internal_id):
        brand = Brand(logo=logo, name=name, description=description, internal_id=internal_id)
        db.session.add(brand)
        db.session.commit()

    @staticmethod
    def update_brand(brand, logo, name, description, internal_id):
        brand.logo = logo
        brand.name = name
        brand.description = description
        brand.internal_id = internal_id
        db.session.commit()

    @staticmethod
    def delete_brand(brand_id):
        brand = BrandController.get_brand_by_id(brand_id)
        if brand:
            db.session.delete(brand)
            db.session.commit()
            return True
        return False
