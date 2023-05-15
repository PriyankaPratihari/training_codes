from pymongo import MongoClient
from script.config import DBConf

MONGO_URI = DBConf.MONGO_URI
try:
    client = MongoClient(MONGO_URI)
    print("connected")
except:
    print("default")

# Creating database
db = client.interns_b2_23

# # Creating document
lib = db.priyanka_lib

# mongodb aggregation pipeline to group units by category and calculate the sum
# pipeline = [
#     {
#         "$group": {
#             "_id": "$category",
#             "total_units": {"$sum": "$units"}
#         }
#     }
# ]
