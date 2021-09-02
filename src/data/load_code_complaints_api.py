####### importing packages ######

import os # use to load file
import pandas as pd # use to create dataframes for data processing

######## setting base and data directories #######

cwd = os.getcwd()

## setting base directory as current directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(cwd)))

## setting BASE_DIR/data as data directory
DATA_DIR = os.path.join(BASE_DIR, 'data') 


## external directory path 
EXT_DIR = os.path.join(DATA_DIR, 'external')


## output file path
code_complaints_file = os.path.join(EXT_DIR, 'code_complaints_dataset.csv')

###### Creating function to create api url and convert it to pandas ########
# Public datasets doesn't need my app token

def SODA_API_to_DF(database_api,select_column,grouping_column):
    url = database_api + '?$query=SELECT%20' + select_column + '%20group%20by%20' + grouping_column
    return pd.read_csv(url)


######## API for Code Complaints and Violations  ###############
# Link: https://data.seattle.gov/Community/Code-Complaints-and-Violations/ez4a-iug7

# Database API can be found on database main page. Please use csv option.
database_api = 'https://data.seattle.gov/resource/ez4a-iug7.csv'

# Select columns needed for analysis
select_column = 'originalzip,count(recordnum)' #create string with columns seperated by comma. Aggregation functions can be used.

# Grouping column if aggregation used
grouping_column = 'originalzip'  #create string with columns seperated by comma.

    
code_complaints_df = SODA_API_to_DF(database_api,select_column,grouping_column)

#############saving dataset in cache folder#####################

code_complaints_df.to_csv(code_complaints_file, index=False)