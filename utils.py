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



def ask_choice(prompt: str, options: list[str]) -> str:
    """
    Prompt the user to select from a list of predefined options.

    Args:
        prompt (str): The question to show before the list.
        options (list): A list of valid options to choose from.

    Returns:
        str: The option selected by the user.
    """
    print(f"\n{prompt}")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    while True:
        choice = input("Enter the number of your choice: ").strip()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(options):
                return index
        print("❌ Invalid input. Please choose a valid number from the list.")