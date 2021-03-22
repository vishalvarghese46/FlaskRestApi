import os
from flask import Flask,jsonify
from flask_restful import Api
from flask_jwt import JWT, jwt_required

from security import authenticate,identity
from resources.user import UserRegister
from resources.items import Item,ItemList
from resources.store import Store,StoreList

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL","sqlite:///data.db")
app.secret_key = 'vishalmon'
api = Api(app)   
jwt = JWT(app,authenticate,identity)

@app.route("/")
def home():
    return jsonify({"message":"Hello, world!"})

api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList,"/items")
api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,"/stores")
api.add_resource(UserRegister,'/register')