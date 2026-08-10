from pyspark.sql.types import StructType, StructField, IntegerType, StringType

ORDERS_SCHEMA = StructType([
    StructField("order_id", IntegerType(), nullable=False),
    StructField("customer_id", IntegerType(), nullable=False),
    StructField("product", StringType(), nullable=False),
    StructField("quantity", IntegerType(), nullable=False),
    StructField("price", IntegerType(), nullable=False),
])

CUSTOMERS_SCHEMA = StructType([
    StructField("customer_id", IntegerType(), nullable=False),
    StructField("name", StringType(), nullable=False),
    StructField("city", StringType(), nullable=False),
])
