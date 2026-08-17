"""
Application-wide constants for the Retail Analytics project.

Only values that are stable across the application should be placed here.
Environment-specific configuration belongs in the configuration module.
"""


# ---------------------------------------------------------------------------
# Dataset names
# ---------------------------------------------------------------------------

ORDERS_DATASET = "orders"
CUSTOMERS_DATASET = "customers"
PRODUCTS_DATASET = "products"


# ---------------------------------------------------------------------------
# File formats
# ---------------------------------------------------------------------------

CSV_FORMAT = "csv"
PARQUET_FORMAT = "parquet"
JSON_FORMAT = "json"


# ---------------------------------------------------------------------------
# Pipeline defaults
# ---------------------------------------------------------------------------

DEFAULT_OUTPUT_MODE = "overwrite"

DEFAULT_PARTITION_COLUMN = "order_date"


# ---------------------------------------------------------------------------
# Data quality
# ---------------------------------------------------------------------------

REQUIRED_ORDER_COLUMNS = (
    "order_id",
    "customer_id",
    "product_id",
    "order_date",
    "quantity",
    "amount",
)

REQUIRED_CUSTOMER_COLUMNS = (
    "customer_id",
    "customer_name",
)

REQUIRED_PRODUCT_COLUMNS = (
    "product_id",
    "product_name",
)
