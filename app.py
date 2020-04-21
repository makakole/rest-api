from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json


app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "your key"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Recruits(db.Model):
    __tablename__ = 'recruits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    personality = db.Column(db.String(200))

    def __init__(self, name, personality):
        self.name = name
        self.personality = personality

@app.route('/recruits', methods= ['GET'])
def home():
    recruits = Recruits.query.all()
    results = {}
    for rec in recruits:
        results.update({"name": rec.name, "personality": rec.personality})

    return results



if __name__ == "__main__":
    app.run()