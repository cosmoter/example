import numpy as np  # library to handle data in a vectorized manner
import random  # library for random number generation
import pandas as pd  # library for data analysis
import requests  # library to handle requests

from geopy.geocoders import Nominatim  # module to convert an address into latitude and longitude values

# libraries for displaying images
from IPython.display import Image
from IPython.core.display import HTML

# tranforming json file into a pandas dataframe library
from pandas.io.json import json_normalize


import folium  # plotting library

print('Folium installed')
print('Libraries imported.')