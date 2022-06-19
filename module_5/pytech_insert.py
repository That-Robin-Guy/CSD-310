from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.aazobyc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students

buffy = {"first_name" : "Buffy", "last_name" : "Summers", "student_id" : "1007"}
buffy_student_id = students.insert_one(buffy).inserted_id

xander = {"first_name" : "Xander", "last_name" : "Harris", "student_id" : "1008"}
xander_student_id = students.insert_one(xander).inserted_id

willow = {"first_name" : "Willow", "last_name" : "Rosenburg", "student_id" : "1009"}
willow_student_id = students.insert_one(willow).inserted_id

print(buffy_student_id)
print(xander_student_id)
print(willow_student_id)

