"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""


import os

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory

from app.forms import AddPropertyForm
from app.models import Property




###
# Routing for your application.
###



def get_uploaded_images():
    upload_dir = app.config.get('UPLOAD_FOLDER')
    return sorted(os.listdir(upload_dir)) 
    
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Ashleigh Palmer")

@app.route('/properties')
def properties():
    """Render a list of all properties."""
    properties_list = Property.query.all()
    return render_template('properties.html', properties=properties_list)



@app.route("/property/<propertyid>")
def property(propertyid):
    # Retrieve the property with the matching id
    property_item = Property.query.filter_by(id=propertyid).first()

    if property_item.photo_filename is not None:
        photo_url = url_for('get_image', filename=property_item.photo_filename) 
    else:
        photo_url = None
    
    # Pass the property and photo URL to the template
    return render_template("indi_property.html", property_item=property_item, photo_url=photo_url)



@app.route('/properties/create', methods=['GET', 'POST'])
def add_property():
    """Add new property to database."""
    form = AddPropertyForm()

    if request.method == 'POST':
        if form.validate_on_submit():
           
            title = form.title.data
            bedrooms = form.bedrooms.data
            bathrooms = form.bathrooms.data
            location = form.location.data
            price = form.price.data
            type = form.type.data
            description = form.description.data
            photo = form.photo.data
            photo_filename = secure_filename(photo.filename)
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo_filename)
            photo.save(photo_path)

                # Create a new Property object
            property_item = Property(
                title=title, 
                bedrooms=bedrooms, 
                bathrooms=bathrooms,
                location=location, 
                price=price,
                type=type,
                description=description, 
                photo_filename =photo_filename)

                # Add the Property object to the database
            db.session.add(property_item)
            db.session.commit()

            flash('Property successfully added!', 'success')
            return redirect(url_for('properties'))

        flash_errors(form)
    return render_template('add_property.html', form=form)


@app.route('/uploads/<filename>')
def get_image(filename):
    print(filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

