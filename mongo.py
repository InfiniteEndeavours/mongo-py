import os
import pymongo

if os.path.exists("env.py"):
    import env

# Import MONGO_URI Secret
MONGO_URI = os.environ.get("MONGO_URI")

# Set Database name
DATABASE = "myFirstDatabase"

# Set collections name
COLLECTION = "celebrities"


def mongo_connect(url):
    """
    Calls the pymongo client method using url
    Prints and returns if successful
    Prints error if not
    """
    try:
        connection = pymongo.MongoClient(url)
        print("Mongo is connected")
        return connection
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s ") % e


# call mongo_connect function using MONGO_URI
conn = mongo_connect(MONGO_URI)

# set coll (db.collection) to myFirstDatabase.celebrities
coll = conn[DATABASE][COLLECTION]

documents = coll.find({"nationality": "american"})

# prints each entry in collection
for doc in documents:
    print(doc)
