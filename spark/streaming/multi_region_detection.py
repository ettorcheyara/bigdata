import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct, col, window

spark = SparkSession.builder \
    .appName("MultiRegionDetectionPseudoStreaming") \
    .getOrCreate()

while True:
    df = spark.read.format("mongodb") \
         .option(
             "spark.mongodb.read.connection.uri",
             "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/learntrack.activities?replicaSet=rs0"
         ) \
         .load()

    suspicious = df.groupBy(
        window(col("timestamp"), "5 minutes"),
        col("student_id")
    ).agg(
        countDistinct("region").alias("region_count")
    ).filter(
        col("region_count") > 1
    )

    suspicious.show(truncate=False)

    # Sauvegarde MongoDB
    suspicious.write \
        .format("mongodb") \
        .option(
            "spark.mongodb.write.connection.uri",
            "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/learntrack.suspicious_users?replicaSet=rs0"
        ) \
        .mode("overwrite") \
        .save()
    
    time.sleep(10)

