import pandas as pd
import numpy as np
import folium
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize
import requests


def clusterlabels(df, num):
    df_loc = df[['latitude','longitude']]
    kmeans_model = KMeans(n_clusters = num).fit(df_loc)
    df_copy = df
    df_copy['label k = ' + str(num)] = kmeans_model.labels_
    print(df_copy)
    return df_copy, list(kmeans_model.cluster_centers_.tolist())

# def createmap(df, num):
#     # Visualizing the plots for K = 5
#     col_index = df.columns.get_loc('label k = ' + str(num))
#     m = folium.Map(location=[df['latitude'].mean(),df['longitude'].mean()], zoom_start=12)
#     for i in range(len(df.index)):
#         if df.iloc[i, col_index] == 0:
#             folium.Marker([df.iloc[i, 1], df.iloc[i, 2]], icon=folium.Icon(color='red')).add_to(m)
#         if df.iloc[i, col_index] == 1:
#             folium.Marker([df.iloc[i, 1], df.iloc[i, 2]], icon=folium.Icon(color='blue')).add_to(m)
#         if df.iloc[i, col_index] == 2:
#             folium.Marker([df.iloc[i, 1], df.iloc[i, 2]], icon=folium.Icon(color='green')).add_to(m)
#         if df.iloc[i, col_index] == 3:
#             folium.Marker([df.iloc[i, 1], df.iloc[i, 2]], icon=folium.Icon(color='orange')).add_to(m)
#         if df.iloc[i, col_index] == 4:
#             folium.Marker([df.iloc[i, 1], df.iloc[i, 2]], icon=folium.Icon(color='purple')).add_to(m)
#     return m


df_Asheville = pd.read_csv('Airbnb_Data_Asheville.csv')
df_cafe_loc1 = pd.read_csv('Asheville Cafe Location Data - Cluster 1.csv')
df_cafe_loc2 = pd.read_csv('Asheville Cafe Location Data - Cluster 2.csv')
df_cafe_loc3 = pd.read_csv('Asheville Cafe Location Data - Cluster 3.csv')

df_temp3, centers3 = clusterlabels(df_Asheville, 3)
df_temp5, centers5 = clusterlabels(df_Asheville, 5)
# map_img = createmap(df_temp3, 3)
print(centers3)

client_id = ''
client_secret = ''

pd.set_option('display.max_columns', 10)
url1_cafe = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20180602&ll={},{}&query=cafe'.format(client_id, client_secret, str(centers3[0][0]), str(centers3[0][1]))
url2_cafe = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20180602&ll={},{}&query=cafe'.format(client_id, client_secret, str(centers3[1][0]), str(centers3[1][1]))
url3_cafe = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20180602&ll={},{}&query=cafe'.format(client_id, client_secret, str(centers3[2][0]), str(centers3[2][1]))
url1_food = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20180602&ll={},{}&query=restaurant'.format(client_id, client_secret, str(centers3[0][0]), str(centers3[0][1]))
url2_food = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20180602&ll={},{}&query=restaurant'.format(client_id, client_secret, str(centers3[1][0]), str(centers3[1][1]))
url3_food = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20180602&ll={},{}&query=restaurant'.format(client_id, client_secret, str(centers3[2][0]), str(centers3[2][1]))
url1_bar = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20180602&ll={},{}&query=bar'.format(client_id, client_secret, str(centers3[0][0]), str(centers3[0][1]))
url2_bar = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20180602&ll={},{}&query=bar'.format(client_id, client_secret, str(centers3[1][0]), str(centers3[1][1]))
url3_bar = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&v=20180602&ll={},{}&query=bar'.format(client_id, client_secret, str(centers3[2][0]), str(centers3[2][1]))

results1 = requests.get(url1_cafe).json()
results2 = requests.get(url2_cafe).json()
results3 = requests.get(url3_cafe).json()
results1_food = requests.get(url1_food).json()
results2_food = requests.get(url2_food).json()
results3_food = requests.get(url3_food).json()
results1_bar = requests.get(url1_fun).json()
results2_bar = requests.get(url2_fun).json()
results3_bar = requests.get(url3_fun).json()

df1_cafe = json_normalize(results1['response']['venues'])
df2_cafe = json_normalize(results2['response']['venues'])
df3_cafe = json_normalize(results3['response']['venues'])
df1_food = json_normalize(results1_food['response']['venues'])
df2_food = json_normalize(results2_food['response']['venues'])
df3_food = json_normalize(results3_food['response']['venues'])
df1_bar = json_normalize(results1_bar['response']['venues'])
df2_bar = json_normalize(results2_bar['response']['venues'])
df3_bar = json_normalize(results3_bar['response']['venues'])
print(df1_cafe.columns, df2_cafe.columns, df3_cafe.columns)

#df1_cafe.to_csv('Asheville Cafe Location Data - Cluster 1.csv')
#df2_cafe.to_csv('Asheville Cafe Location Data - Cluster 2.csv')
#df3_cafe.to_csv('Asheville Cafe Location Data - Cluster 3.csv')
#df1_food.to_csv('Asheville Restaurant Loc Data - Cluster 1.csv')
#df2_food.to_csv('Asheville Restaurant Loc Data - Cluster 2.csv')
#df3_food.to_csv('Asheville Restaurant Loc Data - Cluster 3.csv')
#df1_bar.to_csv('Asheville Fun Loc Data - Cluster 1.csv')
#df2_bar.to_csv('Asheville Fun Loc Data - Cluster 2.csv')
#df3_bar.to_csv('Asheville Fun Loc Data - Cluster 3.csv')

# define a function that takes in a dataframe, then spits out a cluster map in folium

plt.scatter(y = df_temp3['latitude'], x = df_temp3['longitude'], c = df_temp3['label k = 3'], s = df_temp3['price']/10, alpha = 0.5)
plt.title('Asheville Neighborhood Clusters and Price Level')

plt.figure()
plt.scatter(y = df_temp3['latitude'], x = df_temp3['longitude'], c = df_temp3['label k = 3'], s = (df_temp3['reviews_per_month']**2), alpha = 0.5)
plt.title('Asheville Neighborhood Clusters and Number of Reviews')

plt.figure()
plt.scatter(y = df_temp3['latitude'], x = df_temp3['longitude'], c = df_temp3['label k = 3'], s = df_temp3['price']/10, alpha = 0.5)
plt.scatter(y = [centers3[0][0], centers3[1][0], centers3[2][0]], x = [centers3[0][1], centers3[1][1], centers3[2][1]])
plt.scatter(y = df1_cafe['location.lat'], x = df1_cafe['location.lng'], marker='x', color = 'b')
plt.scatter(y = df2_cafe['location.lat'], x = df2_cafe['location.lng'], marker='x', color = 'b')
plt.scatter(y = df3_cafe['location.lat'], x = df3_cafe['location.lng'], marker='x', color = 'b')
plt.title('Asheville Clusters and Nearby Cafes')

plt.figure()
plt.scatter(y = df_temp3['latitude'], x = df_temp3['longitude'], c = df_temp3['label k = 3'], s = df_temp3['price']/10, alpha = 0.5)
plt.scatter(y = [centers3[0][0], centers3[1][0], centers3[2][0]], x = [centers3[0][1], centers3[1][1], centers3[2][1]])
plt.scatter(y = df1_food['location.lat'], x = df1_food['location.lng'], marker='x', color = 'r')
plt.scatter(y = df2_food['location.lat'], x = df2_food['location.lng'], marker='x', color = 'r')
plt.scatter(y = df3_food['location.lat'], x = df3_food['location.lng'], marker='x', color = 'r')
plt.title('Asheville Clusters and Nearby Restaurants')


plt.figure()
plt.scatter(y = df_temp3['latitude'], x = df_temp3['longitude'], c = df_temp3['label k = 3'], s = df_temp3['price']/10, alpha = 0.5)
plt.scatter(y = [centers3[0][0], centers3[1][0], centers3[2][0]], x = [centers3[0][1], centers3[1][1], centers3[2][1]])
plt.scatter(y = df1_fun['location.lat'], x = df1_fun['location.lng'], marker='x', color = 'g')
plt.scatter(y = df2_fun['location.lat'], x = df2_fun['location.lng'], marker='x', color = 'g')
plt.scatter(y = df3_fun['location.lat'], x = df3_fun['location.lng'], marker='x', color = 'g')
plt.title('Asheville Clusters and Nearby Bars')
plt.show()
