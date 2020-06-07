### Project Overview

 Problem statement
You are a die hard Lego enthusiast wishing to collect as many board sets as you can. 
But before that you wish to be able to predict the price of a new lego product before its
price is revealed so that you can budget it from your revenue. Since (luckily!), you are
a data scientist in the making, you wished to solve this problem yourself.
This dataset contains information on lego sets scraped from lego.com. Each observation is a different 
lego set with various features like how many pieces in the set, rating for the set, number of reviews 
per set etc. Your aim is to build a linear regression model to predict the price of a set.

About the Dataset:

You can see that some of the features of review_difficulty, theme_name and Country Name in the data are textual in nature. 
Don't worry, we have made things simple for you with some behind-the-scenes data preprocessing. We have also modified the 
feature of age. You will be learning about all these preprocessing techinques in a later concept. For now let us 
concentrate on getting those Lego sets in your hands soon. :)

new data

The dataset has details of 12261 lego sets with the following 10 features

Feature				Description
age					Which age categories it belongs to
list_price			price of the set (in $)
num_reviews			number of reviews per set
piece_count			number of pieces in that lego set
playstarrating		ratings
review_difficulty	difficulty level of the set
star_rating			ratings
theme_name			which theme it belongs
valstarrating		ratings
country	country 	name


### Learnings from the project

 After completion of this project, I have the better understanding of how to build a linear regression model. 
In this project, I have applied the following concepts.

Train-test split
Correlation between the features
Linear Regression
MSE and R^2 Evaluation Metrics



### Approach taken to solve the problem

 Data loading and splitting
The first step - load the dataset and see how it looks like. Additionally, split it into the train and test set.

Predictor Check!
Let's check the scatter_plot for different features vs target variable list_price. This tells us which features are highly 
correlated with the target variable list_price and help us predict it better.

Reduce feature redundancies!
Features highly correlated with each other adversely affect our lego pricing model. Thus we keep an inter-feature correlation 
threshold of 0.75. If two features are correlated and with a value greater than 0.75, remove one of them.

Is my price prediction ok?
Now let's come to the actual task, using linear regression to predict the price. We will check the model accuracy using 
r^2 score and mse (If the model is bad, please keep extra money for the sets!).

Residual check!
Based on the distance between the true target y_test and predicted target y_pred, also known as the residual the cost function is 
defined. Let's look at the residual and visualize the errors in the model.






