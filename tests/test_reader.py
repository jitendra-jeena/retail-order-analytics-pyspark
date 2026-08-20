import unittest
from pathlib import Path

from pyspark.sql import SparkSession
from src.ingestion.reader import read_csv


class TestReadCSV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = (
            SparkSession.builder
            .master("local[*]")
            .appName("TestReader")
            .getOrCreate()
        )

        cls.test_csv_file = Path("tests/data/orders_test.csv")
        cls.test_parquet_file = Path("tests/data/orders_test_parquet")

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_read_csv_with_order_schema(self):
        df = read_csv(
            spark_session=self.spark,
            input_file=str(self.test_csv_file),
            file_format="csv",
            schema_name="order"
        )

        self.assertIsNotNone(df)

        self.assertEqual(
            df.count(),
            2
        )

        expected_columns = [
            "order_id",
            "customer_id",
            "product",
            "quantity",
            "price",
        ]

        self.assertEqual(
            df.columns,
            expected_columns
        )

    def test_read_csv_without_schema(self):
        df = read_csv(
            spark_session=self.spark,
            input_file=str(self.test_csv_file),
            file_format="csv"
        )

        self.assertIsNotNone(df)

        self.assertEqual(
            df.count(),
            2
        )

        expected_columns = [
            "order_id",
            "customer_id",
            "product",
            "quantity",
            "price",
        ]

        self.assertEqual(
            df.columns,
            expected_columns
        )

    def test_read_parquet(self):
        df = read_csv(
            spark_session=self.spark,
            input_file=str(self.test_parquet_file),
            file_format="parquet"
        )

        self.assertIsNotNone(df)

        self.assertEqual(
            df.count(),
            2
        )

        expected_columns = [
            "order_id",
            "customer_id",
            "product",
            "quantity",
            "price",
        ]

        self.assertEqual(
            df.columns,
            expected_columns
        )

    def test_invalid_schema_name(self):
        with self.assertRaises(Exception):
            read_csv(
                spark_session=self.spark,
                input_file=str(self.test_csv_file),
                file_format="csv",
                schema_name="customer"
            )


if __name__ == "__main__":
    unittest.main()