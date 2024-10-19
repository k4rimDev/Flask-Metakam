from flask import Blueprint, render_template, redirect, url_for

from app.forms.brand_form import BrandForm
from app.forms.manufacturer_form import ManufacturerForm
from app.controllers.brand_controller import BrandController
from app.controllers.manufacturer_controller import ManufacturerController


admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/brands', methods=['GET', 'POST'])
def brands():
    form = BrandForm()
    if form.validate_on_submit():
        BrandController.add_brand(
            logo=form.logo.data,
            name=form.name.data,
            description=form.description.data,
            internal_id=form.internal_id.data
        )
        return redirect(url_for('admin.brands'))
    
    brands = BrandController.get_all_brands()
    return render_template('brand/list.html', form=form, brands=brands)


@admin_bp.route('/manufacturers', methods=['GET', 'POST'])
def manufacturers():
    form = ManufacturerForm()
    if form.validate_on_submit():
        ManufacturerController.add_manufacturer(
            name=form.name.data,
            description=form.description.data,
            country=form.country.data,
            certificates=form.certificates.data,
            internal_id=form.internal_id.data
        )
        return redirect(url_for('admin.manufacturers'))
    
    manufacturers = ManufacturerController.get_all_manufacturers()
    return render_template('manufacturer/list.html', form=form, manufacturers=manufacturers)
