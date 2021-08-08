# OneDeal : An Automobile E-commerce web application

![HomePage](Static%20duplicate/GitHubImages/HomePage.png)

One Deal is a self learning project undertaken to apply Python, HTML, CSS and Flask all into building an application.

One Deal is a prototype of an Automobile E-commerce platform where users can get the best price of their vehicles for resale purpose. Also, users can list their cars for sales and search for vehicles based on the brand, location and most importantly, their budget.

This project involves the use of Python to process the data and create a supervised machine learning regression model to predict prices at the back, HTML and CSS for creating a front end website and flask to connect the model to the website. It also involves the use of Flask form to collect information for vehicles, which is ultimately stored in a car database created using SQLite. 

## **DATA COLLECTION** 
The dataset used for this project has been taken from Kaggle. It is a used car dataset and the link to the dataset is provided below - 
https://www.kaggle.com/avikasliwal/used-cars-price-prediction

![Price Prediction Section](Static%20duplicate/GitHubImages/Price%20Prediction%20Result.png)


## **PRICE PREDICTION ALGORITHM**
1. The Price predicting regression algorithm was created using Python.
2. The following steps were performed to create the model :
   1. *Preliminary data cleaning*:  Steps were performed to correct formatting, identify unnecessary characters, wrongly identified datatypes of features, correct values in    categorical features, etc.
   2. *Exploratory Data Analysis*: Univariate, Bivariate and Multivariate analysis were performed to understand the characteristics of the features, outliers, distributions, relationship of predictors with target i.e price and interrelationship between multiple features. Based on the insights, our preprocessing and model building was done.
   3. *Preprocessing*: Steps like missing values treatment, encoding of categorical features using One Hot Encoding, Target and Frequency encoding and finally scaling were performed before heading to model building.
   4. *Model Building* : Several Baseline linear models like Linear Regression and Non linear models like SVR, KNN, Decision Tree, Random Forest, were created such. Models were evaluated using Root Mean Squared Errors on train and test samples, R2 scores and Variance in train test scores. Feature Selection techniques such as Forward Feature Selection were used to search best features. Ultimately knn performed the best with train r2 of 0.90 and test r2 of 0.88 (lowest variance in results) and rmse of 3.6 on test. On applying grid search to find best parameters, were reduced rmse to 3.3. And on bagging multiple knn models, we got a lowest rmse of 3.24, train r2 of 0.95 and test r2 of 0.90.


## **WEBSITE CREATION**
1. The website was created using HTML for website structure and CSS for formatting and designing elements.
2. The use of Jquery was made to create additional animations and scrolling mechanisms to make the website smoother.
3. Media Queries were used to make the webapp responsive to different screen sizes and devices.
4. NOTE - Despite best efforts, some unwanted formatting changes occur in Apple devices for input boxes and alignment.

![Price Prediction Section](Static%20duplicate/GitHubImages/Search%20Result.png)

## **DATABASE CREATION** 
1. The database for storing listed car information from flaskforms was created using SQLite.
2. The database would be updated once a new car information was successfully passed to the flask form.
3. The new entries could also feature in the search results.

## **DEPLOYMENT**
1. Deployment was performed using Github and Heroku.

The link to the website is provided below - 
https://onedeal.herokuapp.com/
