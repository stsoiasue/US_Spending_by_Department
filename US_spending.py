import json
import requests
import pandas as pd
import numpy as np

import sqlite3
# from uszipcode import ZipcodeSearchEngine

page = 1
url = 'https://api.usaspending.gov/api/v1/awards/?limit=500&page=' + str(page)



params = {
    "filters": [
      {
        "field": "date_signed",
        "operation": "greater_than_or_equal",
        "value": "2017-01-01"
      },
      {
        "field": "date_signed",
        "operation": "less_than",
        "value": "2017-12-31"
      }, 
      {
        "field": "category",
        "operation": "equals",
        "value": "contract"
      },
      {
        "field": "awarding_agency__toptier_agency__cgac_code",
        "operation": "in",
        "value": ["012", "069", "014"]
      },
        {
        "field": "place_of_performance__country_name",
        "operation": "equals",
        "value": "UNITED STATES"
        }]
}

us_data = requests.get(url , json =params).json()

us_dict = {}
us_dict['Awarding_Agency'] = []
us_dict['Subtier_Agency'] = []
us_dict['Subtier_Code'] = []
us_dict['Category'] = []
us_dict['POP_City'] = []
us_dict['POP_State'] = []
us_dict['POP_Zip'] = []
us_dict['Recipient_Name'] = []
us_dict['Total_Obligation'] = []
us_dict['Description'] = []
us_dict['Contract_ID'] = []

next_page = us_data['page_metadata']['has_next_page']
print(next_page)
print(len(us_data['results']))

while next_page:
    for contract in us_data['results']:
        try:
            us_dict['Awarding_Agency'].append(contract['awarding_agency']['toptier_agency']['name'])
        except:
            us_dict['Awarding_Agency'].append(np.nan)
        try:
            us_dict['Subtier_Agency'].append(contract['awarding_agency']['subtier_agency']['name'])
        except:
            us_dict['Subtier_Agency'].append(np.nan)
        try:
            us_dict['Subtier_Code'].append(contract['awarding_agency']['subtier_agency']['subtier_code'])
        except:
            us_dict['Subtier_Code'].append(np.nan)
        try:
            us_dict['Category'].append(contract['category'])
        except:
            us_dict['Category'].append(np.nan)
        try:
            us_dict['POP_City'].append(contract['place_of_performance']['city_name'])
        except:
            us_dict['POP_City'].append(np.nan)
        try:
            us_dict['POP_State'].append(contract['place_of_performance']['state_name'])
        except:
            us_dict['POP_State'].append(np.nan)
        try:
            us_dict['POP_Zip'].append(contract['place_of_performance']['zip5'])
        except:
            us_dict['POP_Zip'].append(np.nan)
        try:
            us_dict['Recipient_Name'].append(contract['recipient']['recipient_name'])
        except:
            us_dict['Recipient_Name'].append(np.nan)
        try:
            us_dict['Total_Obligation'].append(contract['total_obligation'])
        except:
            us_dict['Total_Obligation'].append(np.nan)
        try:
            us_dict['Description'].append(contract['latest_transaction']['assistance_data']['cfda_objectives'])
        except:
            us_dict['Description'].append(np.nan)
        try:
            us_dict['Contract_ID'].append(contract['id'])
        except:
            us_dict['Contract_ID'].append(np.nan)
    page += 1
    url = 'https://api.usaspending.gov/api/v1/awards/?limit=500&page=' + str(page)
    print(us_data['page_metadata']['page'])
    # print(contract['awarding_agency']['toptier_agency']['name'])
    us_data = requests.get(url , json =params).json()
    next_page = us_data['page_metadata']['has_next_page']
        
for contract in us_data['results']:
    print(str(us_data['page_metadata']['page']) + ' LAST PAGE')

    try:
        us_dict['Awarding_Agency'].append(contract['awarding_agency']['toptier_agency']['name'])
    except:
        us_dict['Awarding_Agency'].append(np.nan)
    try:
        us_dict['Subtier_Agency'].append(contract['awarding_agency']['subtier_agency']['name'])
    except:
        us_dict['Subtier_Agency'].append(np.nan)
    try:
        us_dict['Subtier_Code'].append(contract['awarding_agency']['subtier_agency']['subtier_code'])
    except:
        us_dict['Subtier_Code'].append(np.nan)
    try:
        us_dict['Category'].append(contract['category'])
    except:
        us_dict['Category'].append(np.nan)
    try:
        us_dict['POP_City'].append(contract['place_of_performance']['city_name'])
    except:
        us_dict['POP_City'].append(np.nan)
    try:
        us_dict['POP_State'].append(contract['place_of_performance']['state_name'])
    except:
        us_dict['POP_State'].append(np.nan)
    try:
        us_dict['POP_Zip'].append(contract['place_of_performance']['zip5'])
    except:
        us_dict['POP_Zip'].append(np.nan)
    try:
        us_dict['Recipient_Name'].append(contract['recipient']['recipient_name'])
    except:
        us_dict['Recipient_Name'].append(np.nan)
    try:
        us_dict['Total_Obligation'].append(contract['total_obligation'])
    except:
        us_dict['Total_Obligation'].append(np.nan)
    try:
        us_dict['Description'].append(contract['latest_transaction']['assistance_data']['cfda_objectives'])
    except:
        us_dict['Description'].append(np.nan)
    try:
        us_dict['Contract_ID'].append(contract['id'])
    except:
        us_dict['Contract_ID'].append(np.nan)


us_data_df = pd.DataFrame(us_dict)

# us_data_df['Latitude'] = ''
# us_data_df['Longitude'] = ''

# search = ZipcodeSearchEngine()

# for index, row in us_data_df.iterrows():    
#     zipcode = search.by_zipcode(row['POP_Zip'])
#     zip_lat = zipcode['Latitude']
#     zip_lon = zipcode['Longitude']
    
#     if zip_lat == None:
#         res = search.by_city(row['POP_City'])
#         try:
#             row['Latitude']= res[0]['Latitude']
#         except:
#             row['Latitude']= None
#         try:
#             row['Longitude']= res[0]['Longitude']
#         except:
#             row['Longitude']= None
#     else:       
#         row['Latitude'] = zip_lat
#         row['Longitude'] = zip_lon

conn = sqlite3.connect('raw_data_no_lat_lon.sqlite')

us_data_df.to_sql("department_contracts", conn, if_exists="replace")