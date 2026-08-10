from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col


def join_orders_customers(
    spark: SparkSession,
    orders_df: DataFrame,
    customers_df: DataFrame,
    allow_broadcast: bool = True,
) -> DataFrame:
    threshold = "10485760" if allow_broadcast else "-1"  # 10MB default, or force shuffle
    spark.conf.set("spark.sql.autoBroadcastJoinThreshold", threshold)
    return orders_df.join(customers_df, on="customer_id", how="inner")


def compute_order_totals(df: DataFrame, min_price: int = 5000) -> DataFrame:
    return (
        df.filter(col("price") > min_price)
        .withColumn("total_amount", col("quantity") * col("price"))
    )
