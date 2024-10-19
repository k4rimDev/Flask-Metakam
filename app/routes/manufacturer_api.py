from flask import Blueprint, jsonify

from app.controllers.manufacturer_controller import ManufacturerController


manufacturer_bp = Blueprint('manufacturer_api', __name__)


@manufacturer_bp.route('/', methods=['GET'])
def get_all_manufacturers():
    manufacturers = ManufacturerController.get_all_manufacturers()
    return jsonify([{'id': m.id, 'name': m.name, 'description': m.description} for m in manufacturers])


@manufacturer_bp.route('/<int:manufacturer_id>', methods=['GET'])
def get_manufacturer(manufacturer_id):
    manufacturer = ManufacturerController.get_manufacturer_by_id(manufacturer_id)
    if not manufacturer:
        return jsonify({'message': 'Manufacturer not found'}), 404
    return jsonify({'id': manufacturer.id, 'name': manufacturer.name, 'description': manufacturer.description})
