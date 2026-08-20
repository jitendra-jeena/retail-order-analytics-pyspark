from pyspark.sql.types import StructType, StructField, IntegerType, StringType
def get_order_schema():
    ORDERS_SCHEMA = StructType([
        StructField("order_id", IntegerType(), nullable=False),
        StructField("customer_id", IntegerType(), nullable=False),
        StructField("product", StringType(), nullable=False),
        StructField("quantity", IntegerType(), nullable=False),
        StructField("price", IntegerType(), nullable=False),
    ])
    return ORDERS_SCHEMA