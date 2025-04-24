import requests
from config import HEADERS
from utils import build_request_url
from xml_payload import generate_search_xml

# Sends a GET request to the Jonview API using the constructed URL and headers.

# It builds the XML payload, constructs the request URL with parameters,
# and sends an HTTP GET request. If the response status code indicates
# an error, an exception will be raised.

# Returns:
#     str: The response content as a string.


def send_request():
    xml_data = generate_search_xml()
    url = build_request_url(xml_data)
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text
