from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq


def main():
    output_dir = Path("tests/data/orders_test_parquet")
    output_dir.mkdir(parents=True, exist_ok=True)

    table = pa.table(
        {
            "order_id": pa.array([1, 2], type=pa.int32()),
            "customer_id": pa.array([101, 102], type=pa.int32()),
            "product": pa.array(["Laptop", "Mouse"]),
            "quantity": pa.array([2, 3], type=pa.int32()),
            "price": pa.array([500, 25], type=pa.int32()),
        }
    )

    output_file = output_dir / "part-00000.parquet"

    pq.write_table(table, output_file)

    print(f"Parquet file created: {output_file}")


if __name__ == "__main__":
    main()