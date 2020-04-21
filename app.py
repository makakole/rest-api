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
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://qnhhvwecmohebn:20d4d9ca371452624bf721be3991f0b4dbc8122e6a1413cc1932b7b894fccfe2@ec2-52-202-146-43.compute-1.amazonaws.com:5432/d6s315r3ci1224"

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

    return jsonify(recruits)



if __name__ == "__main__":
    app.run()