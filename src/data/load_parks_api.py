#######importing packages######## 

import os # use to load file
import pandas as pd # use to create dataframes for data processing

#########setting base and data directories##########

cwd = os.getcwd()

## setting base directory as current directory
BASE_DIR =  os.path.dirname(os.path.dirname(os.path.dirname(cwd)))

## setting BASE_DIR/data as data directory
DATA_DIR = os.path.join(BASE_DIR, 'data') 

## setting BASE_DIR/data/external as external data directory with API data
EXT_DIR = os.path.join(DATA_DIR, 'external')

## creating external directory. Do not create it if exists
os.makedirs(EXT_DIR,exist_ok=True)

## output file path
parks_file =  os.path.join(EXT_DIR, 'parks_dataset.csv')

######Creating function to create api url and convert it to pandas######
# Public datasets doesn't need my app token

def SODA_API_to_DF(database_api,select_column,grouping_column):
    url = database_api + '?$query=SELECT%20' + select_column + '%20group%20by%20' + grouping_column
    return pd.read_csv(url)

#########API for Seattle Parks and Recreation Park Addresses###########
# Link: https://data.seattle.gov/Parks-and-Recreation/Seattle-Parks-And-Recreation-Park-Addresses/v5tj-kqhc

## assigning variable for constructing the url

# Database API can be found on database main page. Please use csv option.
database_api = 'https://data.seattle.gov/resource/v5tj-kqhc.csv'

# Select columns needed for analysis
select_column = 'zip_code,count(name)' #create string with columns seperated by comma. Aggregation functions can be used.

# Grouping column if aggregation used
grouping_column = 'zip_code'  #create string with columns seperated by comma.

    
parks_df = SODA_API_to_DF(database_api,select_column,grouping_column)



########saving dataset in external folder#########

parks_df.to_csv(parks_file, index=False)

