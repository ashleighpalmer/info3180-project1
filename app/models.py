from . import db

class Property(db.Model):

    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement =True)
    title = db.Column(db.String(80), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo_filename = db.Column(db.String(255), nullable=True)

    # Stores all stored attributes for the Property model
    attrs = ['id', 'title', 'bedrooms', 'bathrooms', 'location', 'price', 'type', 'description', 'photo_filename']

    def __init__(self, title, bedrooms, bathrooms, location, price, type, description, photo_filename):
        """ Class Attributes init """
        super().__init__()
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo_filename = photo_filename
