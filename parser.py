from lxml import etree

# Parses the XML response returned by the Jonview API and prints tag-value pairs.

# This function converts the response string into an XML element tree and iterates
# through the elements to print their tag names and text content. Can be extended
# to extract specific structured data.


# Args:
#     xml_text (str): The raw XML string returned by the API.
def parse_response(xml_text):
    root = etree.fromstring(xml_text.encode("utf-8"))
    for element in root.iter():
        print(f"{element.tag}: {element.text}")
