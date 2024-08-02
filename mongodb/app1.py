

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# database creation
mydb = myclient['mydatabase']

# display database name
print(myclient.list_database_names())

mydb = myclient["abc"]

dblist = myclient.list_database_names()

if "abc" in dblist:
  print("The database exists.")

#creating collection
mycol = mydb["customers"]

# display collection name
print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")