#Plan:
# Do a linear regression on logprice
# Do a polynomial regression with all features poly
# Support Vector Regression maybe
# Tweak Linear Regression if possible
# Repeat LinReg once words are sorted


import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from wordcloud import WordCloud, STOPWORDS
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

pd.set_option('display.max_columns', 20)
airbnb_file = 'AB_US_2020.csv/AB_US_2020.csv'
df_airbnb = pd.read_csv(airbnb_file, low_memory=False)
df_numerical = pd.read_csv('All_Numerical.csv')
df_location = pd.read_csv('Location_Data.csv')
df_numerical_with_words = pd.read_csv('All_Numerical With Words.csv')

# get a correlation matrix
# print(df_numerical.corr())

# Linear Regression, Polynomial Regression, SVM
X_train, X_test, y_train, y_test = train_test_split(df_numerical.drop(['logPrice', 'price'], axis = 1), df_numerical[['logPrice']])

# linear model to establish some sort of baseline.
# r2 falls around 0.3 for both the training and testing set
lm1 = LinearRegression(normalize=True)
lm1.fit(X_train, y_train)
yhat_train = lm1.predict(X_train)
yhat_test = lm1.predict(X_test)
r2score_train = r2_score(y_train, yhat_train)
r2score_test = r2_score(y_test, yhat_test)
print(r2score_test, r2score_train)
# sns.regplot(x = , y= 'logPrice' , data= df_numerical)

# polynomial regression model. Accuracy is only slightly better with r2 value still around 0.3 but better than linear model
lm2 = LinearRegression()
polynom2 = PolynomialFeatures(degree = 2)
X_train_poly = polynom2.fit_transform(X_train)
X_test_poly = polynom2.fit_transform(X_test)
lm2.fit(X_train_poly, y_train)
ypoly_train = lm2.predict(X_train_poly)
ypoly_test = lm2.predict(X_test_poly)
r2polytrain = r2_score(y_train, ypoly_train)
r2polytest = r2_score(y_test, ypoly_test)
print(r2polytrain, r2polytest)


# Support Vector Classifiers because why not? Data go BRRRRRRRR.
# Update: Data doesn't go BRRRRRR because SVM shouldn't be used for big datasets
# Update 2: LinearSVR should be used instead of SVR(kernel = 'linear')
# svr_lin = svm.SVR(kernel='linear')
# svr_lin.fit(X_train, np.ravel(y_train))
# yhat_svr_train = svr_lin.predict(X_train)
# yhat_svr_test = svr_lin.predict(X_test)
# print(r2_score(y_train, yhat_svr_train), r2_score(y_test, yhat_svr_test))
# svr_poly = svm.SVR(kernel= 'poly')
# svr_sig = svm.SVR(kernel = 'sigmoid')
#
# print(X_test_poly)

# models.fit(X_train, y_train)
# yhat_train = models.predict(X_train)
# print(yhat_train, y_train)
# yhat_test = models.predict(X_test)
# print(yhat_test, y_test)


X2_train, X2_test, y2_train, y2_test = train_test_split(df_numerical_with_words.drop(['logPrice', 'price'], axis = 1), df_numerical_with_words[['logPrice']])

# linear model but with the word data
# r2 falls around 0.36 for both the training and testing set
lm3 = LinearRegression(normalize=True)
lm3.fit(X2_train, y2_train)
y2hat_train = lm3.predict(X2_train)
y2hat_test = lm3.predict(X2_test)
r2score_train = r2_score(y2_train, y2hat_train)
r2score_test = r2_score(y2_test, y2hat_test)
print(r2score_test, r2score_train)
