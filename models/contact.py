from utils.db import db
from datetime import datetime
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Contact(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(500), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.created = datetime.utcnow()
        self.deleted = False