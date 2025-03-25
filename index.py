from app import app
from utils.db import db

# Create all tables al correr la app
with app.app_context(): 
    db.init_app(app)
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)