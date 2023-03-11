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


def get_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("Error! No results found.")

    return doc


def add_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    dob = input("Enter date of birth (DD/MM/YYYY): ")
    gender = input("Enter gender: ")
    hair_color = input("Enter hair color: ")
    occupation = input("Enter occupation: ")
    nationality = input("Enter nationality: ")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality
    }

    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key != "_id":
                print(key.capitalize() + ": " + value.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for key, value in doc.items():
            if key != "_id":
                update_doc[key] = input(key.capitalize() + " [" + value + "] > ")

                if update_doc[key] == "":
                    update_doc[key] = value

        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")


def delete_record():
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key != "_id":
                print(key.capitalize() + ": " + value.capitalize())

        print("")
        confirmation = input("Is this the document you want to delete?\nY or N: ")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.delete_one(doc)
                print("Document deleted")
            except:
                print("Error accessing the database.")
        else:
            print("Document not deleted")


def main_loop():
    """
    While True, calls the show_menu function
    Checks option against what is returned from show_menu function
    Prints selected option to terminal
    """
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
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
