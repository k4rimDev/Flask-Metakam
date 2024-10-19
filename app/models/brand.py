from app import db


association_table = db.Table('association',
    db.Column('brand_id', db.Integer, db.ForeignKey('brand.id')),
    db.Column('manufacturer_id', db.Integer, db.ForeignKey('manufacturer.id'))
)


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logo = db.Column(db.String(255))
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    internal_id = db.Column(db.String(50), unique=True)
    manufacturers = db.relationship('Manufacturer', secondary=association_table, back_populates='brands')
