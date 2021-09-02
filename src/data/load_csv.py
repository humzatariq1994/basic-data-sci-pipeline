#!/usr/bin/env python

# make sure to install these packages before running: 
# !pip install pandas

########## importing packages ########### 
import os # use to load file
import pandas as pd # use to create dataframes for data processing

##### setting base and data directories #####
cwd = os.getcwd()

## setting base directory as current directory
BASE_DIR =  os.path.dirname(os.path.dirname(os.path.dirname(cwd)))

## setting BASE_DIR/data as data directory
DATA_DIR = os.path.join(BASE_DIR, 'data') 

## setting data/raw directory for raw batch files
RAW_DIR = os.path.join(DATA_DIR, 'raw') 

## creating DATA_DIR/cache as a directory to store combined batch file

## cache directory path 
CACHE_DIR = os.path.join(DATA_DIR, 'cache')

## creating cache directory. Do not create it if exists
os.makedirs(CACHE_DIR,exist_ok=True)

#######loading and combining all the dataframes together#######

## intializating list to get appended with every for loop run
csv_loop_df = [] 

## making sure that we load only files with the type "csv"
csv_files = [x for x in os.listdir(RAW_DIR) if x.endswith(".csv")]

## loading files 
for filename in csv_files:
    csv_path = os.path.join(RAW_DIR, filename)
    csv_df = pd.read_csv(csv_path)
    csv_loop_df.append(csv_df)

###### creating dataframe from the list created by the for loop ######## 
batch_df = pd.concat(csv_loop_df)

###### loading the combined batch data into csv file to be stored for later use #######
cache = os.path.join(CACHE_DIR, 'house_pricing_dataset.csv')
batch_df.to_csv(cache, index=False)




