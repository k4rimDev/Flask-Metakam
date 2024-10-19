from flask import Blueprint, render_template, redirect, url_for, request, flash

from flask_login import login_required

from app.forms.brand_form import BrandForm
from app.forms.manufacturer_form import ManufacturerForm
from app.controllers.brand_controller import BrandController
from app.controllers.manufacturer_controller import ManufacturerController


admin_bp = Blueprint('admin_client', __name__)


@admin_bp.route('/brands', methods=['GET'])
def brands():    
    brands = BrandController.get_all_brands()
    return render_template('brand/list.html', brands=brands)


@admin_bp.route('/brands/add/', methods=['GET', 'POST'])
@login_required
def add_brand():
    form = BrandForm()
    if form.validate_on_submit():
        BrandController.add_brand(
            logo=form.logo.data,
            name=form.name.data,
            description=form.description.data,
            internal_id=form.internal_id.data
        )
        flash("Brand added successfully!", "success")
        return redirect(url_for('admin_client.brands'))
    
    brands = BrandController.get_all_brands()
    return render_template('brand/add.html', form=form, brands=brands)


@admin_bp.route('/brands/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_brand(id):
    brand = BrandController.get_brand_by_id(id)
    if not brand:
        flash("Brand not found.", "error")
        return redirect(url_for('admin_client.brands'))
    
    form = BrandForm(obj=brand)
    if form.validate_on_submit():
        BrandController.update_brand(
            brand=brand,
            logo=form.logo.data,
            name=form.name.data,
            description=form.description.data,
            internal_id=form.internal_id.data
        )
        flash("Brand updated successfully!", "success")
        return redirect(url_for('admin_client.brands'))
    
    return render_template('brand/edit.html', form=form)


@admin_bp.route('/brands/delete/<int:id>', methods=['POST'])
@login_required
def delete_brand(id):
    if BrandController.delete_brand(id):
        flash("Brand deleted successfully!", "success")
    else:
        flash("Brand not found.", "error")
    return redirect(url_for('admin_client.brands'))


@admin_bp.route('/manufacturers', methods=['GET', 'POST'])
def manufacturers():
    manufacturers = ManufacturerController.get_all_manufacturers()
    return render_template('manufacturer/list.html', manufacturers=manufacturers)


@admin_bp.route('/manufacturers/add/', methods=['GET', 'POST'])
@login_required
def add_manufacturer():
    form = ManufacturerForm()
    if form.validate_on_submit():
        ManufacturerController.add_manufacturer(
            name=form.name.data,
            description=form.description.data,
            country=form.country.data,
            certificates=form.certificates.data,
            internal_id=form.internal_id.data
        )
        flash("Manufacturer added successfully!", "success")
        return redirect(url_for('admin_client.manufacturers'))
    
    manufacturers = ManufacturerController.get_all_manufacturers()
    return render_template('manufacturer/add.html', form=form, manufacturers=manufacturers)


@admin_bp.route('/manufacturers/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_manufacturer(id):
    manufacturer = ManufacturerController.get_manufacturer_by_id(id)
    if not manufacturer:
        flash("Manufacturer not found.", "error")
        return redirect(url_for('admin_client.manufacturers'))
    
    form = ManufacturerForm(obj=manufacturer)
    if form.validate_on_submit():
        ManufacturerController.update_manufacturer(
            manufacturer=manufacturer,
            name=form.name.data,
            description=form.description.data,
            country=form.country.data,
            certificates=form.certificates.data,
            internal_id=form.internal_id.data
        )
        flash("Manufacturer updated successfully!", "success")
        return redirect(url_for('admin_client.manufacturers'))
    
    return render_template('manufacturer/edit.html', form=form)


@admin_bp.route('/manufacturers/delete/<int:id>', methods=['POST'])
@login_required
def delete_manufacturer(id):
    if ManufacturerController.delete_manufacturer(id):
        flash("Manufacturer deleted successfully!", "success")
    else:
        flash("Manufacturer not found.", "error")
    return redirect(url_for('admin_client.manufacturers'))
