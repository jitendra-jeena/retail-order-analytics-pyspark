from pyspark.sql import DataFrame


def repartition_by_column(df: DataFrame, num_partitions: int, column: str | None = None) -> DataFrame:
    if column:
        return df.repartition(num_partitions, column)
    return df.repartition(num_partitions)


def coalesce_partitions(df: DataFrame, num_partitions: int) -> DataFrame:
    return df.coalesce(num_partitions)
