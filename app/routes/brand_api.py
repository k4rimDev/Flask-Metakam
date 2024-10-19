from flask import Blueprint, jsonify

from app.controllers.brand_controller import BrandController


brand_bp = Blueprint('brand_api', __name__)


@brand_bp.route('/', methods=['GET'])
def get_all_brands():
    brands = BrandController.get_all_brands()
    return jsonify([{'id': b.id, 'name': b.name, 'description': b.description} for b in brands])


@brand_bp.route('/<int:brand_id>', methods=['GET'])
def get_brand(brand_id):
    brand = BrandController.get_brand_by_id(brand_id)
    if not brand:
        return jsonify({'message': 'Brand not found'}), 404
    return jsonify({'id': brand.id, 'name': brand.name, 'description': brand.description})
