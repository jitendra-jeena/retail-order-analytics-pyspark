# import libraries

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,IntegerType,StringType
#Build spark session 
spark = SparkSession.builder\
        .appName("RetailOrderAnalytics")\
        .master("local[*]")\
        .getOrCreate()

orders_schema=StructType([
    StructField("order_id",IntegerType(),nullable=False),
    StructField("customer_id",IntegerType(),nullable=False),
    StructField("product",StringType(),nullable=False),
    StructField("quantity",IntegerType(),nullable=False),
    StructField("price",IntegerType(),nullable=False)                            
    ])

df = spark.read.csv("data/raw/orders.csv", header=True, schema=orders_schema)
print("Df schema : \n ")
df.printSchema()
print("Dataframe:\n ")
df.show()

input("Press enter to exit (check spark UI at localhost:4040 now)...")

