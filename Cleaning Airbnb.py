import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from collections import Counter

#  import and read in data

pd.set_option('display.max_columns', 10)
airbnb_file = 'C:/Users/ICD-15/Predict Airbnb Project/AB_US_2020.csv/AB_US_2020.csv'
df_airbnb = pd.read_csv(airbnb_file, low_memory=False)
df_airbnb['reviews_per_month'] = df_airbnb['reviews_per_month'].fillna(0)
# read in airbnb csv and send nulls to 0

print(df_airbnb.dtypes)
# just to get a sense of types

# go through the name column and find the most common words
# finds every word
stopwords = list(STOPWORDS)
comment_words = []                           # create empty list
for val in df_airbnb['name']:                # for loop iterate through dataframe series
    # typecast each val to string
    val = str(val)
    # split the value
    tokens = val.split()                   # tokens is a list of the words in the pd series
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        comment_words.append(tokens[i])

#counts the totals for each word (number of times appeared)
comment_words_nostop = [x for x in comment_words if x not in stopwords]
comment_words_dict = Counter(comment_words_nostop)
comment_list = comment_words_dict.most_common(100)


# the 100 something most common words list
wordlist = []
for item in comment_list:
    wordlist.append(item[0])

print(wordlist)

# a function to turn the word list into a datafram for any data with text column
def getWordData(df):
    '''

    :param df: the dataframe you want to input
    :return: the new appended dataframe
    '''
    df_word = df[['name']]     # read in the dataframe column with text
    for word in wordlist:      # for each word in the global wordlist we're going to check if the row has the word
        bool_list = []
        for value in df['name']:  # for each row we see if it contains the current word
            bool_list.append(int(word in str(value).lower()))    # make sure to take into account case
        df_word[word] = bool_list    # new column is the name of the word plus an integer representation of the boolean column
    df_word.drop(['name'], inplace = True, axis = 1)
    return pd.concat([df, df_word], axis=1)

def CreateDFbyCity(df, city):
    df_city = df[df['city'] == city].drop(['city'], axis = 1)
    df_city = getWordData(df_city).drop(['name'], axis = 1)
    df_city.to_csv('Airbnb_Data_' + city + '.csv')
    return df_city



#  clean the data by removing id, host_id, host_name, neighborhood_group, neighborhood

df_airbnb_drop = df_airbnb.drop(['id', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 'last_review'], axis=1)  # remove a whole lot of info
dummy_dum = pd.get_dummies(df_airbnb_drop['room_type'])  # get all the dummy variables for room type
#  create another table with dummy values for room type

df_bnb_withdummy = pd.concat([df_airbnb_drop, dummy_dum], axis = 1, sort = False)    # concatenate the dummy variables
df_bnb_withdummy.drop(['room_type'], inplace = True, axis = 1)    # drop the room type column now that we have dummies
df_bnb_withdummy['logPrice'] = np.log10(df_bnb_withdummy['price']+1)               # create a new column with logprice
df_bnb_withdummy_words = getWordData(df_bnb_withdummy)                    # add all the numerical word data to the dataframe

#parse the dataframes into different dataframes for each city

#create the list of cities
city_list = list(df_airbnb['city'].unique())
print(city_list)

for city in city_list:
    CreateDFbyCity(df_bnb_withdummy, city)
# df_Austin_num = CreateDFbyCity(df_bnb_withdummy, 'Austin')
# df_Austin_num = getWordData(df_Austin).drop(['name'], axis = 1)


df_bnb_withdummy.drop(['name', 'city'],inplace = True, axis =1 )         # drop the name and city columns
df_bnb_withdummy_words.drop(['name', 'city'],inplace = True, axis =1 )
df_locations = df_bnb_withdummy[['latitude','longitude']]               # get a location dataframe because real estate

# export all the dataframes to new csv files
df_bnb_withdummy_words.to_csv('All_Numerical_Words.csv')
df_bnb_withdummy.to_csv('All_Numerical.csv')
df_locations.to_csv('Location_Data.csv')

