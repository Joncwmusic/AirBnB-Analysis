# Airbnb Analysis

https://www.kaggle.com/kritikseth/us-airbnb-open-data

https://www.kaggle.com/c/house-prices-advanced-regression-techniques

Links to datasets

Goal: So the goal of this is to compare real estate data with air bnb data. Ideally, the question to answer is:
"Is it worth it to buy a house to run a full time airbnb?"

Where we're at:

So basically I've gotten through some modelling. Location Data of nearby attractions does help model accuracy; however,
not by that much. It'll probably require a real estate expert to figure out with location types are important to renters 
or some more research on my part that'd probably be better spent working on another project.

r2scores for regression models on 75/25 test, train split on the whole dataset and zoomed in on Asheville were between .5 and .7 
which is pretty decent for the dataset considering we don't have metrics for cleanliness, picture quality, or even ratings for each aribnb
I imagine some of those less tangible factors are far more important than whether or not your host has 10 airbnbs or just 1.

I haven't integrated the real estate data but I'm also not too hung up on it. I'll still call this a successful learning experience for now.
