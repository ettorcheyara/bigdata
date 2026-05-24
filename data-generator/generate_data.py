import random
from pymongo import MongoClient
from datetime import datetime
import time

client=MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")
db = client.learntrack
activities = db.activities
students = db.students


if students.count_documents({}) == 0:
    for i in range(1, 11):
        students.insert_one({
            "_id": f"S{i:03}",
            "name": f"Student{i}",
            "email": f"student{i}@mail.com",
            "progress": random.randint(0, 100),
            "region": random.choice(["Alger", "Oran", "Constantine"])
        })

print("Étudiants générés ")


types = ["page_view", "quiz_attempt"]
regions = ["Alger", "Oran", "Constantine"]

while True:
    activity = {
        "student_id": f"S{random.randint(1,10):03}",
        "course_id": f"C{random.randint(1,3)}",
        "type": random.choice(types),
        "timestamp": datetime.now(),  
        "region": random.choice(regions)
    }
    activities.insert_one(activity)
    print(f"Activité insérée : {activity}")
    time.sleep(2) 
