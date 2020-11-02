import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS
# import folium

# import and read in data

url = 'https://www.kaggle.com/kritikseth/us-airbnb-open-data/download'

pd.set_option('display.max_columns', 20)
airbnb_file = 'AB_US_2020.csv'
df_airbnb = pd.read_csv(airbnb_file, low_memory=False)

# clean the data by removing id, host_id, host_name, neighborhood_group, neighborhood

df_airbnb_grouped = df_airbnb.groupby(['city'])
df_airbnb_numeric = df_airbnb.drop(['id', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 'city', 'last_review'], axis=1)
dummy_dum = pd.get_dummies(df_airbb_drop['room_type'])

# create another table with dummy values for room type

df_airbnb_withdummy = pd.concat([df_airbnb, dummy_dum], axis = 1, sort = False)

