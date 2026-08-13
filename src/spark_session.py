import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\JITENDRA SINGH JEENA\AppData\Local\Programs\Python\Python312\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\JITENDRA SINGH JEENA\AppData\Local\Programs\Python\Python312\python.exe"
from pyspark.sql import SparkSession

def get_spark_session(app_name="RetailOrderAnalytics"):
    return(
            SparkSession.builder
            .appName(app_name)
            .master("local[*]")
            .getOrCreate()
            )

