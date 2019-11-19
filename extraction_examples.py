# REST API
from urllib import parse
from urllib import request

query_args = {'geom': "POINT(3.3233642578125 55.01953125)"}
encoded_args = parse.urlencode(query_args, safe='()', quote_via=parse.quote)
print('Encoded:', encoded_args)

url = 'https://rest.emodnet-bathymetry.eu/depth_sample?' + encoded_args
print(request.urlopen(url).read().decode('utf-8'))

# WFS (+ data) / WMS (only map)
from owslib.wms import WebMapService
from owslib.wfs import WebFeatureService

wfs11 = WebMapService(url='https://ows.emodnet-humanactivities.eu/wms')
operations = [operation.name for operation in wfs11.operations]
contents = list(wfs11.contents)
methods, options = wfs11.getOperationByName('GetMap').methods, wfs11.getOperationByName('GetMap').formatOptions
img = wfs11.getmap(layers=['portlocations'],
...                     srs='EPSG:4326',
...                     bbox=(-36, 25, 43, 85),
...                     size=(300, 250),
...                     format='image/jpeg'
...                     )
out = open('jpl_mosaic_visb.jpg', 'wb')
out.write(img.read())
out.close()

# REST API (SMHI)
url = "https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/159880/period/latest-months/data.csv"
print(request.urlopen(url).read().decode('utf-8'))