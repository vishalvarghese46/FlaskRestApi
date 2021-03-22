from flask_restful import Resource,reqparse
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store._json(),200
        return {"message":"Store not found in db"},404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message":f"store - {name}, already in the DB!"},400
        store = StoreModel(name)
        store.save_to_db()
        return store._json(), 201

    def delete(self,name):
        store= StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return f"Store {name} deleted successfully!"
        return {"message":"store deleted!"}

class StoreList(Resource):
    def get(self):
        return {"All_stores":[store._json() for store in StoreModel.query.all()]},200
