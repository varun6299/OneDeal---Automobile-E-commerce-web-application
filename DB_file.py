import pandas as pd
from Car import car, DB
import numpy as np

DB.create_all()

data = pd.read_csv("df.csv")

data.drop("Unnamed: 0",axis=1,inplace=True)

for i in data.index:
    Name = data.loc[i,"Name"]
    Location= data.loc[i,"Location"]
    Year= data.loc[i,"Year"]
    Year = round(int(Year),0)
    Kilometers_Driven= data.loc[i,"Kilometers_Driven"]
    Kilometers_Driven = round(Kilometers_Driven,2)
    Fuel_Type= data.loc[i,"Fuel_Type"]
    Transmission= data.loc[i,"Transmission"]
    Owner_Type= data.loc[i,"Owner_Type"]
    Mileage= data.loc[i,"Mileage"]
    Mileage = round(Mileage,2)
    Engine= data.loc[i,"Engine"]
    Engine = round(Engine,2)
    Power= data.loc[i,"Power"]
    Power = round(Power,2)
    Seats= data.loc[i,"Seats"]
    Seats = round(Seats,0)
    Price= data.loc[i,"Price"]
    Price = round(Price,2)
    Brand= data.loc[i,"Brand"]

    car_record = car(Name,Brand,Location,Year,Kilometers_Driven,Fuel_Type,Transmission,Owner_Type,Mileage,Engine,Power,Seats,Price)
    DB.session.add(car_record)
    DB.session.commit()
