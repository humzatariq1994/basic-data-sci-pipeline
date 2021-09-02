########## importing packages ##############

import os # use to load file
import pandas as pd # use to create dataframes for data processing


############ setting base and data directories ###########

cwd = os.getcwd()

## setting base directory as current directory
BASE_DIR =  os.path.dirname(os.path.dirname(os.path.dirname(cwd)))

## setting BASE_DIR/data as data directory
DATA_DIR = os.path.join(BASE_DIR, 'data') 

## cache directory path 
CACHE_DIR = os.path.join(DATA_DIR, 'cache')

## external directory path
EXT_DIR = os.path.join(DATA_DIR, 'external')

## setting working file
working_parks_file =  os.path.join(EXT_DIR, 'parks_dataset.csv')

## setting output file
output_parks_file =  os.path.join(CACHE_DIR, 'parks_dataset_cleaned.csv')

####### creating working parks file dataframe and inspecting it ##########
parks_raw_df = pd.read_csv(working_parks_file)

## setting options to see all columns
pd.set_option('display.max_columns', None)


####### Cleaning and Transforming ##############
'''
Cleaning and Transforming Parks data:
1) Changing zip_code to zipcode so it can join with house_pricing_dataset.
2) Renaming count_name to number_of_parks for clarity
'''
##intializing cleaned_df for transformations
parks_cleaned_df = pd.DataFrame()

##renaming zip_code column to zipcode
parks_cleaned_df['zipcode'] = parks_raw_df['zip_code']

##renaming count_name column to number_of_parks
parks_cleaned_df['number_of_parks'] = parks_raw_df['count_name']



######### storing parks_cleaned_df as a output file ###########

parks_cleaned_df.to_csv(output_parks_file, index=False)