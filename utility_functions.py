# WFS (data) / WMS (map) / CWS (metadata)
from owslib.wms import WebMapService
from owslib.wfs import WebFeatureService
from owslib.wcs import WebCoverageService

# REST API
from urllib import parse
from urllib import request


def ws_init(access_type, endpoint):
    '''Initialise a Web Service object'''
    if access_type == 'wfs': 
        ws = WebFeatureService(endpoint)
    elif access_type == 'wms: 
        ws = WebMapService(endpoint)
    else:
        ws = WebCoverageService(endpoint)
    return ws
  
  
def rest_request(endpoint, query_args):
    '''Send a GET request to REST API endpoint and retrieve results'''
    encoded_args = parse.urlencode(query_args, safe='()', quote_via=parse.quote)
    url = endpoint + encoded_args
    return requests.get(url).content.decode('utf8')