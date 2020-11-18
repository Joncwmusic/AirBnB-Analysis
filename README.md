# DataPortfolio

https://www.kaggle.com/kritikseth/us-airbnb-open-data

https://www.kaggle.com/c/house-prices-advanced-regression-techniques

Links to datasets

Goal: So the goal of this is to compare real estate data with air bnb data. Ideally, the question to answer is:
"Is it worth it to buy a house to run a full time airbnb?"

Outline:

  I. Collect and Clean the BnB Data

    A. Raw Data          Import that stuff
      
    B. Useful Data        From the data what seems important
    
    C. Numerical Data      Get dummies from each categorical variable that seems important
    
    D. Useful Numerical Data   Trim some of the fat
    
    E. Create dummy variables for 100 most common words: 
      
      put all the words into a dictionary and give counts for each of them
      then find the top 100
      For each record in df, create dummy dataframe where
    
    F. Deal with severe outliers       
    
    G. Group by type of bnb      
  
  II. Create Exploratory Visualizations                      
    
    A. Make some Histograms and scatter plots       
    
    B. Create a wordcloud for listing names     
    
    C. aggregate similar visualizations into a single file   
    
    D. Make them pretty     
  
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
  
