from pymongo import MongoClient

client = MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")
db = client.learntrack
activities = db.activities

student_id = "S001"
results = activities.find({"student_id": student_id}).sort("timestamp", -1).limit(20)

print(f"Last 20 activities for {student_id}:")
for r in results:
    print(r)
