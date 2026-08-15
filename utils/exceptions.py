"""
Custom exceptions for the Retail Analytics application.

The exception hierarchy is intentionally small at this stage.
More specific exceptions can be added as the application grows.
"""


class RetailAnalyticsError(Exception):
    """Base exception for the Retail Analytics application.

    All custom application exceptions should inherit from this class.
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class ConfigurationError(RetailAnalyticsError):
    """Raised when application configuration is invalid or missing."""


class DataError(RetailAnalyticsError):
    """Raised when input or processed data is invalid."""


class ProcessingError(RetailAnalyticsError):
    """Raised when an application processing operation fails."""


class IngestionError(RetailAnalyticsError):
    """Raised when data ingestion fails."""


class ValidationError(RetailAnalyticsError):
    """Raised when validation fails."""
