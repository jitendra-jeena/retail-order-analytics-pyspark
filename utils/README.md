# Utilities

Reusable utilities shared across the Retail Analytics application.

## Modules

### `logger.py`
Centralized application logging with:

- Console logging
- Rotating file logging
- Configurable log levels
- Exception stack traces

### `exceptions.py`
Application-specific exception hierarchy.

### `constants.py`
Application-wide stable constants such as dataset names,
file formats, and required columns.

### `paths.py`
Centralized project path construction for:

- Raw data
- Processed data
- Output data
- Checkpoints
- Logs

## Design Principle

Utilities should contain reusable application infrastructure,
not business logic or Spark transformations.

Business-specific transformations belong in the appropriate
pipeline modules.
