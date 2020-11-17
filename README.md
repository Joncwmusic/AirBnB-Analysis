# DataPortfolio

https://www.kaggle.com/kritikseth/us-airbnb-open-data

https://www.kaggle.com/c/house-prices-advanced-regression-techniques

Links to datasets

Goal: So the goal of this is to compare real estate data with air bnb data. Ideally, the question I want to answer is:
"Is it worth it to buy a house to run a full time airbnb?"

Outline:
  I. Collect and Clean the BnB Data
    A. Raw Data                                              #Done
    B. Useful Data                                           #Done
    C. Numerical Data                                        #Done
    D. Useful Numerical Data                                 #Nope
    E. Create dummy variables for 100 most common words      #Nope
    F. Deal with severe outliers                             #Nope
    G. Group by type of bnb                                  #Nope
  II. Create Exploratory Visualizations                      
    A. Make some Histograms and scatter plots                #Done
    B. Create a wordcloud for listing names                  #Done
    C. aggregate similar visualizations into a single file   #Nope
    D. Make them pretty                                      #Nope
  III. Create a predictive price model for Airbnbs
    A. Linear Regression Model
    B. Polynomial Regression Model
    C. Measure accuracy of models with cross validation and R2
    D. Models without the words
    E. Model for each bnb type
  IV. Collect and Clean Housing Data
    A. Raw Data
    B. Mold Data to BnB data by essentially creating a test set
    C. Predict the price

Notes:
  Using Foursquare's API can I find the number of local businesses nearby each airbnb?
  Could I cluster the places within a neighborhood or location in order to sort of see how dense a particular part of town is.
  What if the price of an airbnb goes up or down based on how many other air bnbs are closeby
  In other words for each of the 200K+ datapoints count how many other data points are in the lat long radius (manhattan metric might be best since streets)
  
