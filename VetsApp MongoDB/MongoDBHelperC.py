import pymongo
from tabulate import tabulate

class MongoDBHelper:

    def __init__(self,collection = 'Customer'):
        uri = "mongodb+srv://root:root@vetsapps.5s4zzxd.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri)
        self.db = client['VetsApp']
        self.collection = self.db[collection]
        print("[MongoDB Connected]")

    def insert(self,document):
        result = self.collection.insert_one(document)
        print("Document Inserted...",result)

    def delete(self,query):
        result = self.collection.delete_one(query)
        print("Document Deleted...")

    def fetch(self,query = ""):

            documents = self.db['Customer'].find(query)
            print(tabulate(documents ,headers="keys", tablefmt="grid"))
            """for document in documents:
                print(document)"""

    def update(self,document,query):
        update_query ={"$set": document}

        result = self.collection.update_one(query,update_query)
        print("Document Data Updated ",result)
