from pymongo import MongoClient
from script.config import DBConf

MONGO_URI = DBConf.MONGO_URI
client = None
try:
    client = MongoClient(MONGO_URI)
    print("connected")
except Exception as e:
    print("default"+str(e))

# Creating database
db = client.interns_b2_23

# # Creating document
lib = db.priyanka_lib


