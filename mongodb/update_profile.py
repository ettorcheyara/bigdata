from pymongo import MongoClient

client = MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")
db = client.learntrack
students = db.students

students.update_one(
    {"_id": "S001"},
    {"$set": {"progress": 70, "email": "new@mail.com"}}
)

print("Profile updated")
