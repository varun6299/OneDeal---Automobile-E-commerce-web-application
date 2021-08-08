from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,IntegerField,SelectField

class Listform(FlaskForm):
    Name = StringField('Model',render_kw={'placeholder' : "Enter Name of Model"})
    Brand = SelectField('Brand',choices = [("Ambassador","Ambassador"),("Aston_Martin","Aston Martin"),("Audi","Audi"),("Bentley","Bentley"),("BMW","BMW"),("Chevrolet","Chevrolet"),("Datsun","Datsun"),("Fiat","Fiat"),("Force","Force"),("Ford","Ford"), ("Honda","Honda"),("Hyundai","Hyundai"),("ISUZU","ISUZU"),("Kia","Kia"),("Lamborghini","Lamborghini"),("Land Rover","Land Rover"),("Mahindra","Mahindra"),("Maruti","Maruti"),("Mercedes_Benz","Mercedes Benz"),("MG","MG"),("Mini Cooper","Mini Cooper"),("Nissan","Nissan"),("Porsche","Porsche"),("Renault","Renault"),("Skoda","Skoda"),("Smart","Smart"),("Tata","Tata"),("Toyota","Toyota"),("Volkswagen","Volkswagen"),("Volvo","Volvo"),("Others","Others")])
    Location = SelectField('Current Location',choices = [("Ahmedabad","Ahmedabad"),("Bangalore","Bangalore"),("Chennai","Chennai"),("Coimbatore","Coimbatore"),("Delhi","Delhi"),("Hyderabad","Hyderabad"),("Goa","Goa"),("Jaipur","Jaipur"),("Kanyakumari","Kanyakumari"),("Kochi","Kochi"),("Kolkata","Kolkata"),("Lucknow","Lucknow"),("Mumbai","Mumbai"),("Nagpur","Nagpur"),("Others","Others"),("Pune","Pune"),("Raipur","Raipur"),("Surat","Surat"),("Visakhapatnam","Visakhapatnam"),("Vizag","Vizag")])
    Year = IntegerField('Model Release Year',render_kw={'placeholder' : "Enter Year of Model Release"})
    Kilometers_Driven = IntegerField('Kilometers Driven',render_kw={'placeholder' : "Enter Amount of Kilometers Driven"})
    Fuel_Type = SelectField('Fuel Type',choices = [("Petrol","Petrol"),("Diesel","Diesel"),("CNG","CNG"),("LPG","LPG"),("Electric","Electric"),("EV Hybrid","EV Hybrid")])
    Transmission = SelectField('Transmission method',choices = [("Automatic","Automatic"),("Manual","Manual")])
    Owner_Type = SelectField('No. of Owners (Includes Current & Previous)',choices = [("First","1"),("Second","2"),("Third","3"),("Fourth_and_Above","4 or more")])
    Mileage = StringField('Mileage',render_kw={'placeholder' : "Enter Mileage in km per litre"})
    Engine = IntegerField('Engine',render_kw={'placeholder' : "Enter Engine's cc value"})
    Power = IntegerField('Power',render_kw={'placeholder' : "Enter Engine Power in bhp"})
    Seats = IntegerField('Seating Capacity',render_kw={'placeholder' : "Enter No. of Seats"})
    Expected_Price = StringField('Expected Price',render_kw={'placeholder' : "Enter value in lakhs ex-5.6"})
    Submit = SubmitField('Submit')
