from api_client import send_request
from parser import parse_response
import logging

logging.basicConfig(level=logging.INFO)


def main():
    # Main entry point of the application.

    # Sends the Jonview API request and parses the response.
    # Logs progress and errors for easier debugging and monitoring.

    try:
        logging.info("Sending request to Jonview API...")
        response = send_request()
        logging.info("Response received. Parsing...")
        parse_response(response)
    except Exception as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    main()
