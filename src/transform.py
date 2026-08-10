from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import col

spark = SparkSession.builder\
        .appName("RetailOrderAnalytics")\
        .master("local[*]")\
        .getOrCreate()

orders_schema = StructType([
    StructField("order_id", IntegerType(), nullable=False),
    StructField("customer_id", IntegerType(), nullable=False),
    StructField("product", StringType(), nullable=False),
    StructField("quantity", IntegerType(), nullable=False),
    StructField("price", IntegerType(), nullable=False),
])

df = spark.read.csv("data/raw/orders.csv", header=True, schema=orders_schema)

# transformations -- Noting executes yet 

selected= df.select("order_id","customer_id","product","quantity","price")
expensive_orders = selectd.filter(col("price") > 5000)
with_total = expensive_orders.withcolumn("total_amount",col("quantity")*col("price"))

#action  - this is where it all actually runs
with_total.show()

input("Press enter to exit")
