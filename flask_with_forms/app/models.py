
from datetime import datetime
from app import db

class Client(db.Model):
    __tablename__ = 'Clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<Client: {}:'{}'>".format(self.id, self.name)

class FeatureRequest(db.Model):
    __tablename__ = 'FeatureRequests'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    description = db.Column(db.Text)
    client_id = db.Column(db.Integer, index=True)
    priority = db.Column(db.Integer)
    target_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    product_area = db.Column(db.String(20))

    def __repr__(self):
        return "<FeatureRequest: {}:'{}'>".format(self.id, self.title)
