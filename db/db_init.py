import time
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()

def init_db(app):
    retries = 5
    while retries > 0:
        try:
            with app.app_context():
                db.create_all()
            break
        except OperationalError:
            retries -= 1
            time.sleep(5)