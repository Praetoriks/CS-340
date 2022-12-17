from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username=None, password=None):
        # Initialize the MongoClient. This helps grant access 
        # to the MongoDB databases and collections. 
        
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:53919' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:53919')
        self.database = self.client['AAC']

    # This create method will allow us to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            # Must use "animal" as database as I did it wrong in module 3
            insert = self.database.animal.insert(data)  # data should be the dictionary 
            if insert!=0:
                return True
            else:
                return False           
        else:
            raise Exception("Nothing to save, data parameter is empty")


    # Create method to implement the R in CRUD.
    def read(self,criteria=None):

        # when criteria is not None, this find will return all rows which match criteria
        if criteria:
   
         # {'_id':False} omits the unique ID of each row        
            data = self.database.animal.find(criteria,{"_id":False})

        else:
            
        #if no search criteria, then all the rows will be returned  
            data = self.database.animal.find( {} , {"_id":False})

        return data
