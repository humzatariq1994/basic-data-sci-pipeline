####### importing packages #########

import os # use to load file
import pandas as pd # use to create dataframes for data processing

######### setting base and data directories ###########

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
working_code_complaints_file = os.path.join(EXT_DIR, 'code_complaints_dataset.csv')

## setting output file
output_code_complaints_file = os.path.join(CACHE_DIR, 'code_complaints_dataset_cleaned.csv')

###### creating working code_complaints file dataframe and inspecting it #########
code_complaints_raw_df = pd.read_csv(working_code_complaints_file)

## setting options to see all columns
pd.set_option('display.max_columns', None)

############### Cleaning and Transforming ######################
'''
Cleaning and Transforming Parks data:
1) Changing originalzip to zipcode so it can join with house_pricing_dataset.
2) Renaming count_recordnum to number_of_code_complaints for clarity
3) Removing zipcode=0 and zipcode="" rows
4) Changing zipcode data type to int64

'''
##intializing cleaned_df for transformations
code_complaints_cleaned_df = pd.DataFrame()

##renaming originalzip column to zipcode
code_complaints_cleaned_df['zipcode'] = code_complaints_raw_df['originalzip']

##Renaming count_recordnum to number_of_code_complaints
code_complaints_cleaned_df['number_of_code_complaints'] = code_complaints_raw_df['count_recordnum']

##Removing zipcode=0, zipcode="NaN" and len(zipcode) > 6 rows [zipcode with 0 as decimal should have atleast a lenght of 7]
code_complaints_cleaned_df = code_complaints_cleaned_df.dropna()
code_complaints_cleaned_df = code_complaints_cleaned_df.loc[(code_complaints_cleaned_df!=0.0).all(axis=1)]
code_complaints_cleaned_df = code_complaints_cleaned_df[code_complaints_cleaned_df['zipcode'].map(str).map(len) > 6]

##Changing zipcode data type to int64
code_complaints_cleaned_df['zipcode'] = code_complaints_cleaned_df['zipcode'].astype('int64')


########### storing code_complaints_cleaned_df as a output file ######################

code_complaints_cleaned_df.to_csv(output_code_complaints_file, index=False)

