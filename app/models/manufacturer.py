from app import db


class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    country = db.Column(db.String(80))
    certificates = db.Column(db.String(255))
    internal_id = db.Column(db.String(50), unique=True)
    brands = db.relationship('Brand', secondary='association', back_populates='manufacturers')
