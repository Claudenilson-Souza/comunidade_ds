import pandas as pd
from geopy.geocoders import Nominatim
from matplotlib import pyplot as plt
from matplotlib import gridspec
import plotly.express as px
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import fixed
import time
from multiprocessing import Pool

import defs

data =pd.read_csv ('dataset/house_geo.csv')

data['query'] = data[['lat', 'long']].apply( lambda x: str( x['lat'] ) +
                                            ','
                                            +str( x['long'] ), axis=1 )
df1 = data[['id', 'query']].sample(10)
p = Pool(2)
start = time.process_time()
df1[['place_id', 'osm_type', 'country', 'country_code']] = p.map(defs.get_data, df1.iterrows() )
end = time.process_time()

print(' time{}',end - start)