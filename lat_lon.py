import json
import requests
import pandas as pd
import numpy as np

import sqlite3
from uszipcode import ZipcodeSearchEngine

conn = sqlite3.connect('raw_data_no_lat_lon.sqlite')


us_data_df = pd.read_sql_query("SELECT * FROM department_contracts", conn)

zip_code = pd.DataFrame(us_data_df['POP_Zip'].unique())
zip_code['Latitude'] = ''
zip_code['Longitude'] = ''
zip_code.columns = [
    'POP_Zip',
    'Latitude',
    'Longitude'
]

search = ZipcodeSearchEngine()

for index, row in zip_code.iterrows():    
    zipcode = search.by_zipcode(row['POP_Zip']) 
    row['Latitude'] = zipcode['Latitude']
    row['Longitude'] = zipcode['Longitude']

merged_df = us_data_df.merge(zip_code, how='left', on='POP_Zip')
# merged_df = merged_df[np.isfinite(merged_df['Latitude'])]

conn = sqlite3.connect('data.sqlite')

merged_df.to_sql("department_contracts", conn, if_exists="replace")
merged_df.to_csv('data.csv')
