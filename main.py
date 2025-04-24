import logging
from api_client import (
    send_search_request,
    send_add_reservation_request,
    send_add_passenger_request,
)
from parser import parse_response
from utils import ask_choice

logging.basicConfig(level=logging.INFO)


def handle_add_reservation():
    """
    Handles the 'Add a reservation' action by sending a pre-defined AR request.
    """
    return send_add_reservation_request(
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


def handle_search_reservation():
    """
    Handles the 'Search for reservations' action using a fixed date range.
    """
    return send_search_request(createdatefrom="01-JUL-2016", createdateto="31-JUL-2016")


def handle_add_passenger():
    """
    Handles the 'Add a passenger' action by sending a pre-defined AR request.
    """
    return send_add_passenger_request(
        resitem="23674132", paxnum=4, titlecode="MR", fname="TEST4", lname="SMITH"
    )


def main():
    """
    Main entry point for the Jonview API CLI.
    Allows the user to select and execute various reservation-related actions.
    """
    actions = {
        "Add Reservation": handle_add_reservation,
        "Search for reservations": handle_search_reservation,
        "Add a passenger": handle_add_passenger,
        # Future support (placeholders):
        "Update a reservation": lambda: print("🚧 Update not implemented yet."),
        "Cancel a reservation": lambda: print("🚧 Cancel not implemented yet."),
        "Get reservation details": lambda: print("🚧 Details not implemented yet."),
    }

    action_labels = list(actions.keys())
    selected_index = ask_choice("Select action", action_labels)
    selected_action = action_labels[selected_index]

    logging.info(f"Selected action: {selected_action}")

    try:
        result = actions[selected_action]()
        if isinstance(result, str):  # Only parse response if it's actual XML
            logging.info("Response received. Parsing...")
            parsed_response = parse_response(result)
            logging.info(parsed_response)
            logging.info(f"✅ {selected_action} done.")
    except Exception as e:
        logging.error(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
