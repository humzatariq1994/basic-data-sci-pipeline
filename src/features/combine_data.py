######## importing packages #############

import os # use to load file
import pandas as pd # use to create dataframes for data processing

############ setting base and data directories ###############

cwd = os.getcwd()

## setting base directory as current directory
BASE_DIR =  os.path.dirname(os.path.dirname(os.path.dirname(cwd)))

## setting BASE_DIR/data as data directory
DATA_DIR = os.path.join(BASE_DIR, 'data') 

## cache directory path 
CACHE_DIR = os.path.join(DATA_DIR, 'cache')

## output directory path 
PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')

## setting working file
working_file = os.path.join(CACHE_DIR, 'house_pricing_dataset_cleaned.csv')
working_parks_file =  os.path.join(CACHE_DIR, 'parks_dataset_cleaned.csv')
working_code_complaints_file = os.path.join(CACHE_DIR, 'code_complaints_dataset_cleaned.csv')

## creating cache directory. Do not create it if exists
os.makedirs(PROCESSED_DIR,exist_ok=True)

## setting output file
output_file = os.path.join(PROCESSED_DIR, 'pricing_model_dataset.csv')

###################creating dataframes ########################
house_pricing_df = pd.read_csv(working_file)
parks_df = pd.read_csv(working_parks_file)
code_complaints_df = pd.read_csv(working_code_complaints_file)

#######joining house pricing dataframe and park dataframe together##################

combined_df = pd.merge(house_pricing_df,parks_df,on='zipcode')

########### joining combined dataframe and park dataframe together################

combined_df = pd.merge(combined_df,code_complaints_df,on='zipcode')

################storing combined_df as a output file####################

combined_df.to_csv(output_file, index=False)

