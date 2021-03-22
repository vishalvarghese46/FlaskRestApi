from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
            "price",
            type=float,
            required=True,
            help="This field cannot be left blank!"
        )
    parser.add_argument(
            "store_id",
            type=int,
            required=True,
            help="Every item needs a store Id!"
        )
    
    @jwt_required()
    def get(self, name):
        item =  ItemModel.find_by_name(name)
        if item:
            return item._json()
        return {"Item not found in the database"}, 404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {"message": f"item with name {name} already exists"}, 400 #bad request

        data = Item.parser.parse_args()
        item = ItemModel(name,data["price"],data["store_id"])
        try:
            item.save_to_db()
        except Exception as e:
            return {"message":f"An error occured while inserting the item!{e}"}, 500
        return item._json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message": f"Item deleted, {name}"}      

    def put(self, name):        #put is idempotent as call the put request many times brings back the same result in other words it updated record if already present or creates new one if not present
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name,**data)
            status = 201
        else:
            item.price = data["price"]
            item.store_id = data["store_id"]
        item.save_to_db()
        return item._json(),status


class ItemList(Resource):
    def get(self):        
        return {"item":[item._json() for item in ItemModel.query.all()]}

    