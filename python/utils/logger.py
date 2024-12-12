import os
import logging
from logging.handlers import RotatingFileHandler

def get_logger(log_file_name: str = "default.log", namespace: str = None) -> logging.Logger:
    """
    Creates and configures a logger with a rotating file handler.
    
    This function ensures consistent logging behavior across the project by:
    - Rotating logs to prevent excessive file sizes.
    - Allowing customizable log file names and namespaces for module-specific logging.
    - Ensuring logs are isolated and do not propagate to the root logger.

    Args:
        log_file_name (str): The name of the log file. Defaults to "default.log".
        namespace (str): A unique identifier for the logger. If not provided, 
                         defaults to the log file name without its extension.

    Returns:
        logging.Logger: A configured logger instance.
    """
    # Use the namespace if provided; otherwise, derive the logger name from the log file name
    logger_name = namespace or log_file_name.split('.')[0]
    logger = logging.getLogger(logger_name)

    # Ensure the logger is not reconfigured if already set up
    if not logger.handlers:
        # Define the directory for log files
        log_dir = "python/utils/Logs"
        
        # Check if the log directory exists; create it if necessary
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)  # Ensure the directory is created before attempting to write logs

        # Set the logging level to INFO for standard informational logs
        logger.setLevel(logging.INFO)

        # Prevent duplicate logs by disabling propagation to the root logger
        logger.propagate = False

        # Configure a rotating file handler to manage log file size and backups
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, log_file_name),  # Full path to the log file
            maxBytes=1024 * 1024,  # Maximum log file size before rotation (1 MB)
            backupCount=5          # Keep up to 5 backup files
        )

        # Define the log message format for consistent and detailed output
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)  # Set the handler's logging level to INFO

        # Attach the file handler to the logger
        logger.addHandler(file_handler)

    # Return the fully configured logger instance
    return logger
