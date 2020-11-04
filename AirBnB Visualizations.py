import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


pd.set_option('display.max_columns', 20)
airbnb_file = 'C:/Users/ICD-15/Predict Airbnb Project/AB_US_2020.csv/AB_US_2020.csv'
df_airbnb = pd.read_csv(airbnb_file, low_memory=False)
df_numerical = pd.read_csv('C:/Users/ICD-15/Predict Airbnb Project/All_Numerical.csv')
df_location = pd.read_csv('C:/Users/ICD-15/Predict Airbnb Project/Location_Data.csv')


# Create a word cloud to see which words are most popular amongst airbnb listings
comment_words = ''
for val in df_airbnb['name']:
    # typecaste each val to string
    val = str(val)
    # split the value
    tokens = val.split()
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    comment_words += " ".join(tokens) + " "

stopwords = set(STOPWORDS)
wordcloud = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stopwords, min_font_size = 10).generate(comment_words)
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
