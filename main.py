from api_client import send_search_request, send_add_reservation_request
from parser import parse_response
import logging

logging.basicConfig(level=logging.INFO)


def main():
    # Main entry point of the application.

    # Sends the Jonview API request and parses the response.
    # Logs progress and errors for easier debugging and monitoring.

    try:
        logging.info("Sending request to Jonview API...")
        # response = send_search_request(
        #     createdatefrom="01-JUL-2016", createdateto="31-JUL-2016"
        # )
        response = send_add_reservation_request(
            agentseg="12345",
            commitlevelseg="1",
            paxrecords=[
                {
                    "paxnum": 1,
                    "titlecode": "MR",
                    "fname": "TEST1",
                    "lname": "SMITH",
                    "language": "EN",
                },
                {
                    "paxnum": 2,
                    "titlecode": "MRS",
                    "fname": "TEST2",
                    "lname": "SMITH",
                    "language": "EN",
                },
                {
                    "paxnum": 3,
                    "fname": "TEST3",
                    "lname": "SMITH",
                    "age": "5",
                    "language": "EN",
                },
            ],
            bookrecords=[
                {
                    "booknum": 1,
                    "prodcode": "YTODE",
                    "startdate": "10-DEC-2025",
                    "duration": 2,
                    "note": "This is test booking Nr.1",
                    "paxarray": "YYY",
                },
                {
                    "booknum": 2,
                    "prodcode": "YTOCP",
                    "startdate": "12-DEC-2025",
                    "duration": 3,
                    "note": "This is test booking Nr.2",
                    "paxarray": "YYY",
                },
            ],
        )
        logging.info("Response received. Parsing...")
        parse_response(response)
        print("✅ Request completed successfully.")
    except Exception as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    main()
