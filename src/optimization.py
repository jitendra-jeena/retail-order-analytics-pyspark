from pyspark.sql import DataFrame


def repartition_by_column(df: DataFrame, num_partitions: int, column: str | None = None) -> DataFrame:
    if column:
        return df.repartition(num_partitions, column)
    return df.repartition(num_partitions)


def coalesce_partitions(df: DataFrame, num_partitions: int) -> DataFrame:
    return df.coalesce(num_partitions)


def inspect_partition_sizes(df: DataFrame) -> list[int]:
    """Returns the row count of each partition. Triggers a Spark job (unlike getNumPartitions())."""
    return df.rdd.glom().map(len).collect()

def apply_caching(df: DataFrame) -> DataFrame:
    return df.cache()
