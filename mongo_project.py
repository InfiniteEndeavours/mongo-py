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
        return connection
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s ") % e


def show_menu():
    """
    Prints a menu and asks the user to select an option
    """
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def main_loop():
    """
    While True, calls the show_menu function
    Checks option against what is returned from show_menu function
    Prints selected option to terminal
    :return:
    """
    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


# Create a connection to the Mongo Shard
conn = mongo_connect(MONGO_URI)
# Defines coll as shard.database.collection
coll = conn[DATABASE][COLLECTION]
main_loop()