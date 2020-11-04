import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import and read in data

url = 'https://www.kaggle.com/kritikseth/us-airbnb-open-data/download'

pd.set_option('display.max_columns', 20)
airbnb_file = 'AB_US_2020.csv'
df_airbnb = pd.read_csv(airbnb_file, low_memory=False)

# clean the data by removing id, host_id, host_name, neighborhood_group, neighborhood
# these are all object datatypes and are largely irrelevant

df_airbnb_grouped = df_airbnb.groupby(['city'])
df_airbnb_useful = df_airbnb.drop(['id', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 'last_review'], axis=1)
df_airbnb_drop = df_airbnb.drop(['id', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 'city', 'last_review'], axis=1)
dummy_dum = pd.get_dummies(df_airbnb_useful['room_type'])

# create another table with dummy values for room type

df_airbnb_withdummy = pd.concat([df_airbnb_useful, dummy_dum], axis = 1, sort = False)
df_airbnb_numeric = df_airbnb_withdummy.drop(['name', 'room_type'], axis = 1)
df_airbnb_numeric.to_csv('All_Numerical.csv')

