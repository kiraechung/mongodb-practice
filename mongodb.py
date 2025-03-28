#!/workspaces/mongodb-practice/env/bin/python3
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os

# mongohost should look something like 'mongodb+srv://cluster0.xxxxx.mongodb.net/'
MONGOUSER = os.getenv('MONGOUSER')
MONGOPASS = os.getenv('MONGOPASS')
MONGOHOST = os.getenv('MONGOHOST')

client = MongoClient(MONGOHOST, username=MONGOUSER, password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
db = client.dyd6mg #gets the database
friends = db["friends"] #creates a collection called "friends" in database dyd6mg


item_1 = {
  "name" : "Miya Livingston",
  "year" : "2",
  "major" : "computer science",
  "met" : "class",
}

item_2 = {
  "name" : "Mia Tan",
  "year" : "3",
  "major" : "cognitive science",
  "met" : "hometown",
}

item_3 = {
  "name" : "Emily Le",
  "year" : "3",
  "major" : "political & social thought",
  "met" : "club",
}
item_4 = {
  "name" : "Fan Lin",
  "year" : "4",
  "major" : "biology",
  "met" : "club",
}

item_5 = {
  "name" : "Christy Guan",
  "year" : "2",
  "major" : "commerce",
  "met" : "club",
}

somefriends=[item_1,item_2,item_3,item_4,item_5]

friends.insert_many(somefriends)

threeitems = friends.find({"met": "club"})

for doc in threeitems:
     print(doc)
