import requests
from parser import parse_response
from utils import build_request_url

HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}


def send_jonview_request(xml_data: str) -> str:
    """
    Sends an HTTP GET request to the Jonview API with the given XML message.

    Args:
        xml_data (str): The full XML payload to embed in the URL.

    Returns:
        str: The response text from the API.

    Raises:
        requests.exceptions.HTTPError: If the request fails or returns an error code.
    """
    try:
        url = build_request_url(xml_data)
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(
                f"Request failed with status code {response.status_code}"
            )
        if response.status_code == 200:
            result = parse_response(response.text)
            if result.get("status") == "F":
                raise requests.exceptions.HTTPError(
                    f"Request failed with message: {result.get('errmsg')}"
                )
        return response.text
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.HTTPError(f"An error occurred: {e}")


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
    Sends an Add Reservation (AR) request to the Jonview API.
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

    return send_jonview_request(xml_data)


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
    """
    Sends a search request (RS) to the Jonview API.
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

    return send_jonview_request(xml_data)


def send_add_passenger_request(
    resitem: str,
    paxnum: int,
    titlecode: str,
    fname: str,
    lname: str,
    age: str = "",
    language: str = "EN",
    paxseq: str = "",
) -> str:
    """
    Sends an Add Passenger (AP) request to the Jonview API.
    """
    xml_data = f"""<message>
    <actionseg>AP</actionseg>
    <resinfoseg>
        <resitem>{resitem}</resitem>
    </resinfoseg>
    <paxseg>
        <paxrecord>
            <paxnum>{paxnum}</paxnum>
            <paxseq>{paxseq}</paxseq>
            <titlecode>{titlecode}</titlecode>
            <fname>{fname}</fname>
            <lname>{lname}</lname>
            <age>{age}</age>
            <language>{language}</language>
        </paxrecord>
    </paxseg>
</message>"""

    return send_jonview_request(xml_data)
