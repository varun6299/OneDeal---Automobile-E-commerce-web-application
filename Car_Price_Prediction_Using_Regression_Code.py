#!/usr/bin/env python
# coding: utf-8

# # Problem Statement

# Our goal is to make a machine learning model that can predict the price of the user car.

# # Data Description

# - Name : The brand and model of the car.
# - Location : The location in which the car is being sold or is available for purchase.
# - Year : The year or edition of the model.
# - Kilometers Driven : The total kilometres driven in the car by the previous owner(s) in KM.
# - Fuel Type : The type of fuel used by the car. (Petrol, Diesel, Electric, CNG, LPG)
# - Transmission : The type of transmission used by the car. (Automatic / Manual)
# - Owner Type : Whether the ownership is Firsthand, Second hand or other.
# - Mileage : The standard mileage offered by the car company in kmpl or km/kg
# - Engine : The displacement volume of the engine in CC.
# - Power : The maximum power of the engine in bhp
# - Seats : The number of seats in the car.
# - Price : The price of the used car in INR Lakhs.

# # Importing packages and dataset

# In[1]:


import pandas as pd
import numpy as np
import scipy.stats as stats
import pickle

data = pd.read_csv('car_train.csv')


## Data Cleaning

data.Seats.replace(to_replace=0,value=data.Seats.median(),inplace=True)


data.drop("Unnamed: 0",axis=1,inplace=True)


data.Year = data.Year.astype("object")

data["Brand"] = data.Name.apply(lambda x:x.split()[0])

data.drop("Name",axis=1,inplace=True)

data.Brand.replace({"Isuzu":"ISUZU","Land":"Land Rover","Mini":"Mini Cooper"},inplace=True)

data["Model_Age"] = 2021 - data.Year.apply(lambda x:int(x))

data.drop("Year",axis=1,inplace=True)


## EDA
### PREPROCESSING : Missing Value Treatment

data.drop("New_Price",axis=1,inplace=True)


for i in ["Mileage","Engine","Power"]:
    data[i].replace({np.nan:"nan nan"},inplace=True)


for i in ["Mileage","Engine","Power"]:
    data[i] = data[i].apply(lambda x:x.split()[0])


for i in ["Mileage","Engine","Power"]:
    data[i].replace({"nan":"0"},inplace=True)
    data[i].replace({"null":"0"},inplace=True)


for i in ["Mileage","Engine","Power"]:
    data[i] = data[i].astype("float")


for i in ["Mileage","Engine","Power"]:
    data[i].replace({0:np.nan},inplace=True)


for i in ["Mileage","Engine","Power","Seats"]:
    data[i].fillna(data[i].median(),inplace=True)

num_cols = ["Kilometers_Driven","Mileage","Engine","Power","Model_Age","Seats","Price"]


## EDA - Preprocessing
### Encoding


data = pd.get_dummies(data,columns=["Fuel_Type","Transmission"])

data1 = data.copy()

for i in data.index:
    if data.loc[i,"Owner_Type"] == "First":
        data.loc[i,"Owner_Type"] = 1
    if data.loc[i,"Owner_Type"] == "Second":
        data.loc[i,"Owner_Type"] = 2
    if data.loc[i,"Owner_Type"] == "Third":
        data.loc[i,"Owner_Type"] = 3
    if data.loc[i,"Owner_Type"] == "Fourth & Above":
        data.loc[i,"Owner_Type"] = 4

data.Owner_Type = data.Owner_Type.astype("int64")

data.Brand = data.Brand.map(data.Brand.value_counts(normalize=True))

data.Location = data.Location.map(data.groupby("Location")["Price"].median())


## EDA - Preprocessing
### Scaling


data2 = data.copy()

num_cols = ["Location","Owner_Type","Mileage","Engine","Power","Seats","Brand","Model_Age"]


X = data.copy()
X_sc = data.copy()
Y = data.Price


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

SC = StandardScaler()
SC = StandardScaler().fit(X_sc[list(num_cols)])
X_sc[list(num_cols)] = SC.transform(X_sc[list(num_cols)])


x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.30,random_state=20)
x_train_sc,x_test_sc,y_train,y_test = train_test_split(X_sc,Y,test_size=0.30,random_state=20)


## MODEL BUILDING


from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import BaggingRegressor


features = ['Mileage',
 'Power',
 'Seats',
 'Brand',
 'Model_Age',
 'Fuel_Type_CNG',
 'Fuel_Type_Electric',
 'Fuel_Type_LPG',
 'Fuel_Type_Petrol',
 'Transmission_Automatic',
 'Transmission_Manual']

num_features = ['Mileage',
 'Power',
 'Seats',
 'Brand',
 'Model_Age']


Bag_Knn_model = KNeighborsRegressor(n_neighbors=10,weights="distance",metric="manhattan")
final_model = BaggingRegressor(base_estimator=Bag_Knn_model,random_state=0,max_features=11,bootstrap_features=True).fit(x_train_sc[list(features)],y_train)

Scalar = StandardScaler().fit(x_train[num_features],y_train)


brand_availability = dict(data1.Brand.value_counts(normalize=True))


### SAVING THE FUNCTION AND MODELS
Scaler_Function = pickle.dump(Scalar,open("Scaler.pkl","wb"))
Model_Function = pickle.dump(final_model,open("Model.pkl","wb"))
Brand_Dict = pickle.dump(brand_availability,open("Brand_price.pkl","wb"))
