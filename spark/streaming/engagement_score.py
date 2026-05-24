from pyspark.sql import SparkSession
from pyspark.sql.functions import count
import time

spark = SparkSession.builder \
    .appName("EngagementScore") \
    .getOrCreate()

while True:
    df = spark.read.format("mongodb") \
         .option("spark.mongodb.read.connection.uri", "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/learntrack.activities?replicaSet=rs0") \
        .option("spark.mongodb.database", "learntrack") \
        .option("spark.mongodb.collection", "activities") \
        .load()

    score_df = df.groupBy("student_id") \
        .count() \
        .withColumnRenamed("count", "engagement_score")

    score_df.show(truncate=False)

    score_df.write \
        .format("mongodb") \
        .option(
            "spark.mongodb.write.connection.uri",
            "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/learntrack.engagement_scores?replicaSet=rs0"
        ) \
        .mode("overwrite") \
        .save()


    time.sleep(10)  

