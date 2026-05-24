from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")
db = client.learntrack
activities = db.activities

activity = {
    "student_id": "S001",
    "course_id": "C001",
    "type": "quiz_attempt",
    "timestamp": datetime.now(),
    "region": "constantine"
}

activities.insert_one(activity)
print("Activity inserted")
