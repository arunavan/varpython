# import MongoClient
from pymongo import MongoClient
 
 
# Creating a client
client = MongoClient('localhost', 27017)
 
# Creating a database name GFG
db = client['GFG']
print("Database is created !!")