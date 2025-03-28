#!/workspaces/mongodb-practice/env/bin/python3
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os

# mongohost should look something like 'mongodb+srv://cluster0.xxxxx.mongodb.net/'
MONGOUSER = os.getenv('MONGOUSER')
MONGOPASS = os.getenv('MONGOPASS')
MONGOHOST = os.getenv('MONGOHOST')
print(MONGOUSER)

#client = MongoClient(MONGOHOST, username=MONGOUSER, password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
#db = client.dyd6mg #gets the database
#friends = db["friends"] #creates a collection called "friends" in database dyd6mg


#item_1 = {
#  "_id" : "1000",
#  "name" : "Miya Livingston",
#  "year" : "2",
#  "major" : "computer science",
#  "met" : "class",
#}

#item_2 = {
#  "_id" : "1001",
#  "name" : "Mia Tan",
#  "year" : "3",
#  "major" : "cognitive science",
#  "met" : "hometown",
#}

#item_3 = {
#  "_id" : "1002",
#  "name" : "Emily Le",
#  "year" : "3",
#  "major" : "political & social thought",
#  "met" : "club",
#}

#item_4 = {
#  "_id" : "1003",
#  "name" : "fan lin",
#  "year" : "4",
#  "major" : "biology",
#  "met" : "club",
#}

#item_5 = {
#  "_id" : "1004",
#  "name" : "Christy Guan",
#  "year" : "2",
#  "major" : "commerce",
#  "met" : "club",
#}

#friends.insert_many([item_1,item_2,item_3,item_4,item_5])

#threeitems = friends.find({"met": "club"})

#print(threeitems)



