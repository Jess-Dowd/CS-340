from pymongo import MongoClient

class AnimalShelter(object):

    def __init__(self, username, password):
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33853
        DB = 'AAC'
        COL = 'animals'

        self.client = MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}/?authSource=admin')
        self.database = self.client[DB]
        self.collection = self.database[COL]


    def create(self, data):
        if data is not None:
            insertSuccess = self.database.animals.insert_one(data)
            if insertSuccess.acknowledged:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, searchData={}):
        return list(self.database.animals.find(searchData))

        
    def update(self, searchData, updateData):
        if searchData and updateData:
            try:
                result = self.database.animals.update_many(searchData, {"$set": updateData})
                return result.modified_count
            except Exception as e:
                print("Update failed:", e)
                return 0
        else:
            raise Exception("Search or update data is empty")

    def delete(self, deleteData):
        if deleteData:
            try:
                result = self.database.animals.delete_many(deleteData)
                return result.deleted_count
            except Exception as e:
                print("Delete failed:", e)
                return 0
        else:
            raise Exception("Delete data is empty")

