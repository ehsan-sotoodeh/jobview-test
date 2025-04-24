from lxml import etree

# Parses the XML response returned by the Jonview API and returns tag-value pairs.

# This function converts the response string into an XML element tree and iterates
# through the elements to collect their tag names and text content into a dictionary.
# Can be extended to extract specific structured data.

# Args:
#     xml_text (str): The raw XML string returned by the API.
# Returns:
#     dict: A dictionary containing tag-value pairs from the XML.
def parse_response(xml_text):
    root = etree.fromstring(xml_text.encode("utf-8"))
    result = {}
    for element in root.iter():
        result[element.tag] = element.text
    return result
