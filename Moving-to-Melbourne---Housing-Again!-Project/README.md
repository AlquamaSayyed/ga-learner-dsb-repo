### Project Overview

 Your friend from Iowa, whose housing problem you solved, is now moving to Melbourne for a new assignment Down Under. 
As you have solved his Iowa housing problem so well, he wants you to solve his Melbourne housing problem too. 
Armed with your new-found expertise in regularization, let's work on the Melbourne housing data using regularized regression. 
Each observation is a different house attribute with various features, like the number of properties that exist in the suburb, 
land size, building size, governing council for the area, real estate agent, price of the house, etc.

About the Dataset:

The dataset has details of 6830 house entries with the following 16 features

Feature							Description
Rooms							Number of rooms
Type							Property type
Price							Price in dollars
Method							Property status
SellerG	Real 					Estate Agent
Distance						Distance from CBD
Postcode						Code of the area
Bathroom						Number of Bathrooms
Car								Number of carspots
Landsize						Land Size
BuildingArea					Building Size
YearBuilt						The year in which home was built
CouncilArea						Governing council for the area
Longtitude						The angular distance of a place east or west
Regionname						General Region (West, North West, North, Northeast …etc)
PropertyCount					Number of properties that exist in the suburb



### Learnings from the project

 After completing this project, we will have a better understanding of how to build a regularized regression model. 
In this project, we will apply the following concepts.

Train-test split

Correlation between the features

Linear Regression

Polynomial Regressor

Lasso Regressor

Ridge Regressor

R^2Evaluation Metrics



### Approach taken to solve the problem

 Data Loading and Splitting
The first step - you know the drill by now - is to load the dataset and see what it looks like. Additionally, split it 
into train and test set.

Prediction Using Linear regression
Now let's come to the actual task,i.e, predicting the price of the house using linear regression. We will check the
model performance using r^2 score.

Prediction Using Lasso
In this task, let's predict the price of the house using a lasso regressor. Check if there is any improvement in the prediction.

Prediction Using Ridge
There wasn't a clear improvement after applying the lasso regressor; that once again drives home the point that it's not
necessary that the model will improve after regularization.
Now, let's check the house price prediction using a ridge regressor.

Prediction Using Cross-Validation
Now let's predict the house price using cross-validated estimators which are the part of the 
Model selection: choosing estimators and their parameters.

Prediction Using Polynomial Regressor
As you can see that there is very less improvement(~1%), even after applying the regularization and cross-validation score. 
Now let's perform the prediction using a polynomial regressor to generate second-degree polynomial features.



