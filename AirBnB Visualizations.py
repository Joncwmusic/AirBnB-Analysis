import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


pd.set_option('display.max_columns', 20)
airbnb_file = 'AB_US_2020.csv/AB_US_2020.csv'
df_airbnb = pd.read_csv(airbnb_file, low_memory=False)
df_numerical = pd.read_csv('All_Numerical.csv')
df_location = pd.read_csv('Location_Data.csv')


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


# histograms of data. If data has heavy right skew, log is applied to kind of approximate normality

ax1 = df_numerical['number_of_reviews'].plot(kind='hist', title='Num of Reviews')
plt.figure()
ax2 = np.log2(df_numerical['number_of_reviews']+1).plot(kind = 'hist', title = 'Log Num of Reviews')
plt.figure()
ax3 = np.log10(df_numerical['reviews_per_month']+1).plot(kind = 'hist', title = 'Reviews Per Month')
plt.figure()
ax4 = np.log2(df_numerical['calculated_host_listings_count']+1).plot(kind = 'hist', title = 'host listings count')
plt.figure()
ax5 = df_numerical['availability_365'].plot(kind = 'hist', title = 'availability', bins = 36)
# some spikes in the histogram around 90 days, 180 days, and 365 days.
plt.show()
