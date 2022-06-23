from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.aazobyc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students

print("\n--- Displaying Students Documents From find() Query --- \n")
docs = db.students.find({})
for doc in docs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"])
    print("\n")


cordelia = {"first_name" : "Cordelia", "last_name" : "Chase", "student_id" : "1010"} 

cordelia_student_id = students.insert_one(cordelia).inserted_id 

print("\n--- Insert Statement ---\n")
 
print(cordelia_student_id) 
print("\n")

doc = db.students.find_one({"student_id": "1010"}) 
print("--- New Inserted Document --- \n")
print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"]) 


bye = db.students.delete_one({"student_id" : "1010"}) 
print("\n--- Deleted Student ID: 1010 ---\n")
docs = db.students.find({})
for doc in docs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"])
    print("\n")
