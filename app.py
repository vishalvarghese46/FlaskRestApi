from flask import Flask,jsonify
from flask_restful import Api
from flask_jwt import JWT, jwt_required

from security import authenticate,identity
from resources.user import UserRegister
from resources.items import Item,ItemList
from resources.store import Store,StoreList

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.secret_key = 'vishalmon'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()
    
jwt = JWT(app,authenticate,identity)

@app.route("/")
def home():
    return jsonify({"message":"Hello, world!"})

api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList,"/items")
api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,"/stores")
api.add_resource(UserRegister,'/register')

if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True,port=5000)