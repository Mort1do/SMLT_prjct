import sqlite3
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api()
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test1.db"
db.init_app(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)


class Brands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Models(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))


class Clothes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String, nullable=False)
    season = db.Column(db.String)
    sex = db.Column(db.Integer, nullable=False)
    #образ жизни
    description = db.Column(db.String)
    photo = db.Column(db.LargeBinary)
    model_id = db.Column(db.Integer, db.ForeignKey('models.id'))


with app.app_context():
   db.create_all()



class App(Resource):
    def get(self, id):
        get_clothes = db.session.get(Clothes, id)
        get_model = db.session.get(Models, get_clothes.model_id)
        get_brand = db.session.get(Brands, get_model.brand_id)
        print(get_clothes.name, get_clothes.price)
        return {"name": get_clothes.name,
                "brand": get_brand.name,
                "model": get_model.name,
                "color": get_clothes.color,
                "price": get_clothes.price,
                "type": get_clothes.type,
                "season": get_clothes.season,
                "sex": get_clothes.sex,
                "description": get_clothes.description,
                }

    def post(self, id):
        return 200

    def put(self, id):
        return 200

    def delete(self, id):
        return 200


api.add_resource(App, "/<int:id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host='127.0.0.1')