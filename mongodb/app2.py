# importing module 
from pymongo import MongoClient 
  
# creation of MongoClient 
client=MongoClient() 
  
# Connect with the portnumber and host 
client = MongoClient("mongodb://localhost:27017/") 
  
# Access database 
mydb = client['mydb'] 
 
print(client.list_database_names()) 
"""
# Access collection of the database 
mycollection=mydb['myTable'] 
  
# dictionary to be added in the database 
record={ 
"title": "MongoDB and Python",  
"description": "MongoDB is no SQL database",  
"viewers": "104" 
} 
  
# inserting the data in the database 
rec = mydb.myTable.insert(record)
"""