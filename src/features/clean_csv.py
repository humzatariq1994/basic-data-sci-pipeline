########## importing packages ###########

import os # use to load file
import pandas as pd # use to create dataframes for data processing

############## setting base and data directories #################

cwd = os.getcwd()

## setting base directory as current directory
BASE_DIR =  os.path.dirname(os.path.dirname(os.path.dirname(cwd)))

## setting BASE_DIR/data as data directory
DATA_DIR = os.path.join(BASE_DIR, 'data') 

## cache directory path 
CACHE_DIR = os.path.join(DATA_DIR, 'cache')

## setting working file
working_file = os.path.join(CACHE_DIR, 'house_pricing_dataset.csv')

## setting output file
output_file = os.path.join(CACHE_DIR, 'house_pricing_dataset_cleaned.csv')


###### creating working file dataframe and inspecting it ############
raw_df = pd.read_csv(working_file)

## setting options to see all columns
pd.set_option('display.max_columns', None)

####### Cleaning and Transforming Data #############
'''
Cleaning and Transforming House Pricing data:
1) Cutting T000000 from date column as all the times are set at 12am and adding no extra value
2) Changing date datatype from object to date so it can be used for visualization
3) Discarding null values if any
'''
##intializing cleaned_df for transformations
cleaned_df = raw_df

##removing T000000 substring from date column and retaining date of the string
cleaned_df['date'] = cleaned_df['date'].str[:8]

##changing date column datatype from object to datetime
cleaned_df['date'] = pd.to_datetime(cleaned_df['date'])

##discard any null values
cleaned_df = cleaned_df.dropna()

########## storing cleaned_df as a output file ###############

cleaned_df.to_csv(output_file, index=False)