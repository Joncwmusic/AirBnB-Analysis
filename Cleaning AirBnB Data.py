# so the goal here is to clean up the data as it's coming in
# This means:
# 1. Importing the data into a pandas dataframe
# 2. Removing superficial information like ID's, names, neighborhood names 
# 2.5 which should be covered by latitude longitude data anyways but it might also be helpful to group by city or neighborhood
# 3. Make sure the top 100 words are dummy variabled

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#
# import and read in data
#

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

#
#       Text Cleaning
#

# This creates a massive list with all the words in the dataframe column
comment_words = []                           # create empty string
for val in df_airbnb['name']:                # for loop iterate through dataframe series
    # typecast each val to string
    val = str(val)
    # split the value
    tokens = val.split()                   # tokens is a list of the words in the pd series
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        comment_words.append(tokens[i])

        
# this is to get rid of the 'uhhs' and 'umms' fo the data
stopwords = list(STOPWORDS)
comment_words_nostop = [x for x in comment_words if x not in stopwords]
comment_words_dict = Counter(comment_words_nostop)  # creates a dictionary for each word and their respective word counts
comment_list = comment_words_dict.most_common(100) # returns the top 100 words with their counts


# the 100 something most common words list without the counts
wordlist = []
for item in comment_list:
    wordlist.append(item[0])

# print(wordlist) - this should be double checked justfor a sanity check


# create the word 'dummy variable' dataframe that enters 1 is the word is in the 'name' column and 0 if it's not
df_word = df_airbnb[['name']]
# print(df_word) - sanity check

# for each word in the word list we're going to see if the word is in the name entry for each row
for word in wordlist:
    bool_list = []
    for value in df_airbnb['name']:
        bool_list.append(int(word in str(value).lower()))
    df_word[word] = bool_list

# combine everything into one big dataframe
df_airbnb_with_words = pd.concat([df_airbnb, df_word], axis=1)
df_airbnb_allnums = pd.concat([df_bnb_withdummy, df_airbnb_with_words], axis=1)

#save the files
df_airbnb_with_words.to_csv('Airbnb With Words')
df_airbnb_allnums.to_csv('All Numerical With Words')
