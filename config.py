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


HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
