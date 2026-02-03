"""AWS Lambda entry point for snow-flask-whoami."""

import os
import sys

# Add parent directory to path for snow_flask_core imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import awsgi
from dotenv import load_dotenv

from snow_flask_core import create_app
from snow_flask_core.logging_config import setup_logging

load_dotenv()
setup_logging()

app = create_app()


def lambda_handler(event: dict, context: object) -> dict:
    """AWS Lambda handler function."""
    return awsgi.response(app, event, context)
