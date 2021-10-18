from pymongo import MongoClient
from bson.objectid import ObjectId 
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username='aacuser', password='cat'):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:27017/AAC' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:27017')
        self.database = self.client['AAC']

# create method to implement the C in CRUD.

    def create(self, data):

        if data is not None:

            insert = self.database.animals.insert(data)  # data should be dictionary   
            if insert!=0:
                return True
            else:
                return False

        else:

            raise Exception("Nothing to save, because data parameter is empty")

# Create this create method to implement the R in CRUD.
    
    def read(self,query=None):
        
        # criteria is not None then it returns all that match the criteria
        if query:
            
            data = self.database.animals.find(query,{"_id":False})
            
        else:
            #if there is no criteria to find, then rows return
            data = self.database.animals.find({},{"_id":False})

        return data
    
# Create this Update method to implement the U in CRUD

    def update(self, data, updatedData):
        
        # criteria is not None then it updates all that match the criteria
            
        if data is not None:
            
            updated = self.database.animals.update_many(data, updatedData)
            
            return dumps(self.read(updatedData))
        
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# Create this Delete method to implement the D in CRUD

    def delete(self, data):
        
        # criteria is not None then it deletes all that match the criteria
        
        if data is not None:
            deleted = self.database.animals.delete_many(data)
            
            return dumps(self.read(data))
        
        else:
            raise Exception("Nothing to save, because data parameter is empty")
