from pymongo import MongoClient
from bson.objectid import ObjectId 
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username='aacuser', password='cat'):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:39715/AAC' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:39715')
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
    
    def read(self,criteria=None):
        
        # criteria is not None then it returns all that matches the criteria
        if criteria:
            
            data = self.database.animals.find(criteria,{"_id":False})
        else:
            #if there is no criteria to find, then rows return
            data = self.database.animals.find({},{"_id":False})

        return data
