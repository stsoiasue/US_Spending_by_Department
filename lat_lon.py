import json
import requests
import pandas as pd
import numpy as np

import sqlite3
from uszipcode import ZipcodeSearchEngine

conn = sqlite3.connect('us_data3.sqlite')

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

conn = sqlite3.connect('final_dataset.sqlite')

zip_code.to_sql("department_contracts", conn, if_exists="replace")