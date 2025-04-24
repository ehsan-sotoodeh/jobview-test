import requests
from utils import build_request_url

HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}


def send_add_reservation_request(
    agentseg: str,
    commitlevelseg: str,
    sessionid: str = "",
    referencecheck: str = "N",
    productnamedisplay: str = "Y",
    cancellationpolicydisplay: str = "Y",
    advisorynotedisplay: str = "Y",
    durationdescrdisplay: str = "Y",
    vaofferdisplay: str = "Y",
    refitem: str = "PartnerRefNr",
    attitem: str = "AddReservationSample",
    resitem: str = "",
    paxrecords: list = [],
    bookrecords: list = [],
) -> str:
    """
    Sends an Add Reservation (AR) request to the Jonview API with dynamic values.

    This function builds the required XML payload including segments for agent,
    options, reservation info, passenger list, and booking details.
    The request is sent as a GET request with all parameters included in the URL.

    Args:
        agentseg (str): Agent ID.
        commitlevelseg (str): Commit level.
        sessionid (str): Session identifier (optional).
        referencecheck (str): Reference check flag.
        productnamedisplay (str): Whether to display product name.
        cancellationpolicydisplay (str): Whether to display cancellation policy.
        advisorynotedisplay (str): Whether to show advisory notes.
        durationdescrdisplay (str): Whether to show duration description.
        vaofferdisplay (str): Whether to show value-added offers.
        refitem (str): Reference item.
        attitem (str): Attachment item.
        resitem (str): Reservation item (optional).
        paxrecords (list): List of dicts representing each passenger.
        bookrecords (list): List of dicts representing each booking.

    Returns:
        str: The raw XML response as a string.
    """

    paxseg = ""
    for pax in paxrecords:
        paxseg += f"""
        <paxrecord>
            <paxnum>{pax.get("paxnum", "")}</paxnum>
            <paxseq>{pax.get("paxseq", "")}</paxseq>
            <titlecode>{pax.get("titlecode", "")}</titlecode>
            <fname>{pax.get("fname", "")}</fname>
            <lname>{pax.get("lname", "")}</lname>
            <age>{pax.get("age", "")}</age>
            <language>{pax.get("language", "")}</language>
        </paxrecord>"""

    bookseg = ""
    for book in bookrecords:
        bookseg += f"""
        <bookrecord>
            <booknum>{book.get("booknum", "")}</booknum>
            <bookseq>{book.get("bookseq", "")}</bookseq>
            <prodcode>{book.get("prodcode", "")}</prodcode>
            <startdate>{book.get("startdate", "")}</startdate>
            <duration>{book.get("duration", "")}</duration>
            <note>{book.get("note", "")}</note>
            <paxarray>{book.get("paxarray", "")}</paxarray>
        </bookrecord>"""

    xml_data = f"""<message>
    <actionseg>AR</actionseg>
    <agentseg>{agentseg}</agentseg>
    <commitlevelseg>{commitlevelseg}</commitlevelseg>
    <optionseg>
        <sessionid>{sessionid}</sessionid>
        <referencecheck>{referencecheck}</referencecheck>
        <productnamedisplay>{productnamedisplay}</productnamedisplay>
        <cancellationpolicydisplay>{cancellationpolicydisplay}</cancellationpolicydisplay>
        <advisorynotedisplay>{advisorynotedisplay}</advisorynotedisplay>
        <durationdescrdisplay>{durationdescrdisplay}</durationdescrdisplay>
        <vaofferdisplay>{vaofferdisplay}</vaofferdisplay>
    </optionseg>
    <resinfoseg>
        <refitem>{refitem}</refitem>     
        <attitem>{attitem}</attitem>
        <resitem>{resitem}</resitem>
    </resinfoseg>
    <paxseg>{paxseg}
    </paxseg>
    <bookseg>{bookseg}
    </bookseg>
</message>"""

    url = build_request_url(xml_data)
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text


def send_search_request(
    createdatefrom: str,
    createdateto: str,
    startdatefrom: str = "",
    startdateto: str = "",
    reference: str = "",
    firstname: str = "",
    lastname: str = "",
    status: str = "OK",
    source: str = "ALL",
) -> str:
    """Sends a search request to the API with the specified parameters and returns the response.

    Args:
        createdatefrom (str): The starting creation date for the search filter (in YYYY-MM-DD format).
        createdateto (str): The ending creation date for the search filter (in YYYY-MM-DD format).
        startdatefrom (str, optional): The starting date for the search filter (in YYYY-MM-DD format). Defaults to an empty string.
        startdateto (str, optional): The ending date for the search filter (in YYYY-MM-DD format). Defaults to an empty string.
        reference (str, optional): A reference string to filter the search. Defaults to an empty string.
        firstname (str, optional): The first name to filter the search. Defaults to an empty string.
        lastname (str, optional): The last name to filter the search. Defaults to an empty string.
        status (str, optional): The status to filter the search. Defaults to "OK".
        source (str, optional): The source to filter the search. Defaults to "ALL".

    Returns:
        str: The response text from the API.


    Raises:
        requests.exceptions.HTTPError: If the HTTP request fails or returns an error status code.
    """

    xml_data = f"""<message>
        <actionseg>RS</actionseg>
        <searchseg>
            <startdatefrom>{startdatefrom}</startdatefrom>
            <startdateto>{startdateto}</startdateto> 
            <createdatefrom>{createdatefrom}</createdatefrom>
            <createdateto>{createdateto}</createdateto>
            <reference>{reference}</reference>
            <firstname>{firstname}</firstname>
            <lastname>{lastname}</lastname>
            <status>{status}</status>
            <source>{source}</source>
        </searchseg>
        </message>"""

    url = build_request_url(xml_data)
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text
