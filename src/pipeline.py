import argparse

from src.spark_session import get_spark_session
from src.ingestion import load_orders, load_customers
from src.transformations import join_orders_customers, compute_order_totals


def run_pipeline() -> None:
    spark = get_spark_session()

    orders_df = load_orders(spark)
    customers_df = load_customers(spark)

    orders_df = compute_order_totals(orders_df)
    result_df = join_orders_customers(spark, orders_df, customers_df)

    result_df.show()

    return spark  # hand the session back so the entry point can decide when to stop it


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hold",
        action="store_true",
        help="Keep the Spark session alive after the pipeline runs, so the Spark UI stays reachable at localhost:4040.",
    )
    args = parser.parse_args()

    spark = run_pipeline()

    if args.hold:
        input("Pipeline complete. Spark UI live at localhost:4040. Press Enter to stop the session...")

    spark.stop()
