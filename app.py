from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jnztgtduagkkeg:23ae23b5fc4fa8646489302f341d08af6380ca4c22b9d2a2e4e382e0eff36a70@ec2-54-159-112-44.compute-1.amazonaws.com:5432/dbuj69j3s984fn'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Recruits(db.Model):
    __tablename__ = 'recruits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    personality = db.Column(db.String(200))

    def __init__(self, name, personality):
        self.customer = customer
        self.personality = personality

@app.route('/recruits', methods= ['GET'])
def home():
    recruits = Recruits.query.all()

    return jsonify(recruits)



if __name__ == "__main__":
    app.run()