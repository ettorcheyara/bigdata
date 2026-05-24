from pyspark.sql import SparkSession
from pyspark.sql.functions import count


spark = SparkSession.builder \
    .appName("DailyReports") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.3.0") \
    .getOrCreate()



df = spark.read.format("mongodb") \
    .option("spark.mongodb.read.connection.uri", "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/learntrack.activities?replicaSet=rs0")  \
    .load()


report = df.groupBy("course_id").agg(count("*").alias("total_activities"))



report.write.format("mongodb") \
    .option("spark.mongodb.write.connection.uri", "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/learntrack.daily_reports?replicaSet=rs0") \
    .mode("append") \
    .save()


report.show()


spark.stop()
