### Primitive import scripts for various file formats

## CSV, TXT (No Metadata)
# https://pypi.org/project/pandas/
pip install pandas
# example usage
import pandas as pd
df = pd.read_csv(file_path, sep=",")

## RDF
# https://pypi.org/project/rdflib/
pip install rdflib
# example usage
import rdflib
g=rdflib.Graph()
g.load('http://dbpedia.org/resource/Semantic_Web')

## DARWIN CORE
# https://pypi.org/project/python-dwca-reader/
pip install python-dwca-reader
# example usage
from dwca.read import DwCAReader

with DwCAReader('gbif-results.zip') as dwca:
   print("Core data file is: {}".format(dwca.descriptor.core.file_location)) # => 'occurrence.txt'
   # creates a Pandas dataframe
   core_df = dwca.pd_read('occurrence.txt', parse_dates=True)

## NETCDF
# https://pypi.org/project/netcdf/
pip install netcdf
# example usage
from netcdf import netcdf as nc
root, is_new = nc.open('file_*.nc')
data = nc.getvar(root, 'data')
print("Matrix values: ", data[:])

## GEOTIFF (requires GDAL package)
# https://pypi.org/project/georasters/
pip install georasters
# example usage
import georasters as gr
raster = './data/slope.tif'
data = gr.from_file(raster)

## KML, Shapefiles, Esri Geodatabase, Raster
# https://pypi.org/project/geopandas/
pip install geopandas
# https://pypi.org/project/Fiona/
pip install Fiona
# example usage
import geopandas as gpd
gpdf = geopandas.read_file(file_path)

## For everything else
# https://gdal.org/download.html#conda
git clone https://github.com/OSGeo/GDAL.git
conda install -c conda-forge gdal
# example usage
from osgeo import ogr
inDataSource = ogr.Open("parcels.shp")

# Conversion between file formats
# https://gdal.org/programs/ogr2ogr.html
# example usage
ogr2ogr -f "ESRI Shapefile" destination_data.shp "source-data.json"

# Getting any information available about an unknown source format
# https://gdal.org/programs/ogrinfo.html#ogrinfo
# example usage
ogrinfo wrk/SHETLAND_ISLANDS.NTF
  
