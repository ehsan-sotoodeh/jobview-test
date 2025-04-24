from urllib.parse import urlencode
from config import BASE_URL, ACTION_CODE, CLIENT_LOC_SEQ, USER_ID, PASSWORD

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
