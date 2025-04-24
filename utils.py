from urllib.parse import urlencode
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Base configuration pulled from environment
BASE_URL = os.getenv("BASE_URL")
ACTION_CODE = os.getenv("ACTION_CODE")
CLIENT_LOC_SEQ = os.getenv("CLIENT_LOC_SEQ")
USER_ID = os.getenv("USER_ID")
PASSWORD = os.getenv("PASSWORD")


# Constructs the full URL with query parameters for the API request.

# Args:
#     xml_message (str): The XML message to be embedded as a URL parameter.

# Returns:
#     str: The full API endpoint URL with all required query parameters.


def build_request_url(xml_message):
    params = {
        "actioncode": ACTION_CODE,
        "clientlocseq": CLIENT_LOC_SEQ,
        "userid": USER_ID,
        "password": PASSWORD,
        "message": xml_message,
    }
    return f"{BASE_URL}?{urlencode(params)}"
