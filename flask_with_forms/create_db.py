
from app import db
from app.models import Client
db.create_all()

db.session.add(Client(name='Client A'))
db.session.add(Client(name='Client B'))
db.session.add(Client(name='Client C'))
db.session.commit()
