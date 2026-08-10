from pyspark.sql import DataFrame, SparkSession
from src.schemas import ORDERS_SCHEMA, CUSTOMERS_SCHEMA


def load_orders(spark: SparkSession, path: str = "data/raw/orders.csv") -> DataFrame:
    return spark.read.csv(path, header=True, schema=ORDERS_SCHEMA)


def load_customers(spark: SparkSession, path: str = "data/raw/customers.csv") -> DataFrame:
    return spark.read.csv(path, header=True, schema=CUSTOMERS_SCHEMA)
