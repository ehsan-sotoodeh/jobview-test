# Generates the XML payload for the Jonview API search request.

# This XML specifies search parameters such as creation date range,
# status, and source. It forms the body of the query used in the API call.


# Returns:
#     str: A string containing the complete XML message.
def generate_search_xml():
    return """<message>
 <actionseg>RS</actionseg>
 <searchseg>
     <startdatefrom></startdatefrom>
     <startdateto></startdateto> 
     <createdatefrom>01-JUL-2016</createdatefrom>
     <createdateto>31-JUL-2016</createdateto>
     <reference></reference>
     <firstname></firstname>
     <lastname></lastname>
     <status>OK</status>
     <source>ALL</source>
 </searchseg>
</message>"""
