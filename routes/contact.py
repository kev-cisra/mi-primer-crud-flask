from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db import db 
from models.contact import Contact

contacts = Blueprint('contacts', __name__)  # Cambiado de 'contacs' a 'contacts'

@contacts.route('/')
def index():
    Contacts = Contact.query.filter_by(deleted=False).all()

    return render_template('index.html', contacts=Contacts)

@contacts.route('/new', methods=['POST'])
def new():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]

    newContact = Contact(name, email, phone)

    db.session.add(newContact)
    db.session.commit()

    flash('Contact added successfully', 'success')

    return redirect(url_for('contacts.index'))

@contacts.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    contactUp = Contact.query.filter_by(id=id).first()
    if request.method == 'POST':
        contactUp.name = request.form["name"]
        contactUp.email = request.form["email"]
        contactUp.phone = request.form["phone"]

        db.session.commit()

        flash('Contact updated successfully', 'success')

        return redirect(url_for('contacts.index'))
    
    return render_template('update.html', contact=contactUp)

@contacts.route('/delete/<id>')
def delete(id):
    contact = Contact.query.filter_by(id=id).first()
    contact.deleted = True
    db.session.commit()

    flash('Contact deleted successfully', 'success')
    
    return redirect(url_for('contacts.index'))

@contacts.route('/about')
def about():
    return render_template('about.html')