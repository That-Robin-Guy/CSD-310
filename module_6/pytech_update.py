from unittest import result
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


result = db.students.update_one({"student_id" : "1007"}, {"$set" : {"last_name" : "Summers III"}})
print(result)
print("\n")

up = db.students.find_one({"student_id" : "1007"})
print("--- Displaying Updated Student Document From find_one() Query ---\n")
print("Student ID: " + up["student_id"] + "\nFirst Name: " + up["first_name"] + "\nLast Name: " + up["last_name"])