from pyspark.sql import SparkSession

# Initialize a basic Spark session
spark = SparkSession.builder \
    .appName("My Spark Application") \
    .getOrCreate()

print("Spark session is ready! 🚀")
