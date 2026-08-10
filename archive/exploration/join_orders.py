from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType , IntegerType, StringType
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("RetailOrderAnalytics") \
    .master("local[*]") \
    .getOrCreate()

orders_schema = StructType([
    StructField("order_id", IntegerType(), False),
    StructField("customer_id", IntegerType(), False),
    StructField("product", StringType(), False),
    StructField("quantity", IntegerType(), False),
    StructField("price", IntegerType(), False),
])

customers_schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("city", StringType(), False),
])

orders = spark.read.csv("data/raw/orders.csv", header=True, schema=orders_schema)
customers = spark.read.csv("data/raw/customers.csv", header=True, schema=customers_schema)

joined = orders.join(customers,
                     on = "customer_id",
                     how= "inner"
                     )

joined.show()
input("Press enter to exit (check Spark UI now)...")
