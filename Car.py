from flask import Flask , url_for , render_template , request, redirect,session, flash
import pickle
import numpy as np
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  and_ , or_
from flask_migrate import Migrate
from forms import Listform


app = Flask(__name__,template_folder='Template',static_folder='Static')

app.config['SECRET_KEY'] = 'my_secret_key'

basedir = os.path.abspath(os.path.dirname(__name__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(app)
Migrate(app,DB)
########################### CREATING THE DATABASE ###########################

class car(DB.Model):

    __tablename__ = 'cars'

    id = DB.Column(DB.Integer,primary_key=True)
    Name = DB.Column(DB.String,nullable=False)
    Brand = DB.Column(DB.String,nullable=False)
    Location= DB.Column(DB.String,nullable=False)
    Year= DB.Column(DB.Integer,nullable=False)
    Kilometers_Driven= DB.Column(DB.Float,nullable=False)
    Fuel_Type = DB.Column(DB.String,nullable=False)
    Transmission= DB.Column(DB.String,nullable=False)
    Owner_Type= DB.Column(DB.String,nullable=False)
    Mileage= DB.Column(DB.Float,nullable=False)
    Engine= DB.Column(DB.Float,nullable=False)
    Power= DB.Column(DB.Float,nullable=False)
    Seats= DB.Column(DB.Integer,nullable=False)
    Price= DB.Column(DB.Float,nullable=False)

    def __init__(self,Name,Brand,Location,Year,Kilometers_Driven,Fuel_Type,Transmission,Owner_Type,Mileage,Engine,Power,Seats,Price):
        self.Name = Name
        self.Brand = Brand
        self.Location = Location
        self.Year = Year
        self.Kilometers_Driven = Kilometers_Driven
        self.Fuel_Type = Fuel_Type
        self.Transmission = Transmission
        self.Owner_Type = Owner_Type
        self.Mileage = Mileage
        self.Engine = Engine
        self.Power = Power
        self.Seats = Seats
        self.Price = Price

################ LOADING REQUIRED SAVED FILES FOR MODEL ######################
arr = pickle.load(open('array.pkl','rb'))
model = pickle.load(open('Model.pkl','rb'))
Scalar = pickle.load(open('Scaler.pkl','rb'))
Brand_Price = pickle.load(open('Brand_price.pkl','rb'))

################################# APP #################################


@app.route('/',methods=['GET','POST'])
def Index():

    form = Listform()

    if form.validate_on_submit():
        flash("Congrats! You completed the listing process of your Car.")

        Name = form.Name.data
        Brand = form.Brand.data
        Location = form.Location.data
        Year = form.Year.data
        Kilometers_Driven = form.Kilometers_Driven.data
        Fuel_Type = form.Fuel_Type.data
        Transmission = form.Transmission.data
        Owner_Type = form.Owner_Type.data
        Mileage = form.Mileage.data
        Engine = form.Engine.data
        Power = form.Power.data
        Seats = form.Seats.data
        Expected_Price = form.Expected_Price.data
        Car_record = car(Name,Brand,Location,Year,Kilometers_Driven,Fuel_Type,Transmission,Owner_Type,Mileage,Engine,Power,Seats,Expected_Price)
        DB.session.add(Car_record)
        DB.session.commit()

        return redirect(url_for('Index'))

    return render_template('Flex.html',form = form)




@app.route('/Search_Result')
def Search_Result():
    brand = request.args.get("Brand")
    price = request.args.get("Price")
    location = request.args.get("Location")
    if price == '0-10':
        car_list = car.query.filter(and_(car.Brand == brand,car.Price < 10,car.Location==location)).order_by(car.Price.asc()).limit(10)
    elif price == '10-20':
        car_list = car.query.filter(and_(car.Brand == brand,car.Price>10,car.Price <=20,car.Location==location)).order_by(car.Price.asc()).limit(10)
    elif price == '20-50':
        car_list = car.query.filter(and_(car.Brand == brand ,car.Price>20,car.Price<=50,car.Location==location)).order_by(car.Price.asc()).limit(10)
    elif price == '50-100':
        car_list = car.query.filter(and_(car.Brand == brand,car.Price>50,car.Price<=100,car.Location==location)).order_by(car.Price.asc()).limit(10)
    else:
        car_list = car.query.filter(and_(car.Brand == brand, car.Price>100,car.Location==location)).order_by(car.Price.asc()).limit(10)

    counts = car_list.count()

    if counts > 0:
        return render_template('Search_result.html',car_list = car_list)
    else:
        return render_template('Search_Results_No_result.html')




@app.route('/Price_Prediction',methods=['GET','POST'])
def Price_Prediction():
    mileage = float(request.args.get('Mileage'))
    power = float(request.args.get('Power'))
    seats = int(request.args.get('Seats'))
    brand_name = request.args.get('Brand')
    brand_avg_price = float(Brand_Price[brand_name])
    model_age = 2021 - int(request.args.get('Year'))
    fuel = request.args.get('Fuel')
    if fuel  == 'CNG':
        fuel_Type_CNG = 1
        fuel_Type_Electric = 0
        fuel_Type_LPG = 0
        fuel_Type_Petrol = 0
    elif fuel  == 'Diesel':
        fuel_Type_CNG = 0
        fuel_Type_Electric = 0
        fuel_Type_LPG = 0
        fuel_Type_Petrol = 0
    elif fuel  == 'LPG':
        fuel_Type_CNG = 0
        fuel_Type_Electric = 0
        fuel_Type_LPG = 1
        fuel_Type_Petrol = 0
    elif fuel  == 'Petrol':
        fuel_Type_CNG = 0
        fuel_Type_Electric = 0
        fuel_Type_LPG = 0
        fuel_Type_Petrol = 1
    else:
        fuel_Type_CNG = 0
        fuel_Type_Electric = 1
        fuel_Type_LPG = 0
        fuel_Type_Petrol = 0
    transmission = request.args.get('Transmission')
    if transmission == 'Manual':
        transmission_Manual = 1
        transmission_Automatic = 0
    else:
        transmission_Manual = 0
        transmission_Automatic = 1

    user_input = arr([mileage,power,seats,brand_avg_price,model_age,fuel_Type_CNG,fuel_Type_Electric,fuel_Type_LPG,fuel_Type_Petrol,transmission_Automatic,transmission_Manual])
    user_input[:5] =  Scalar.transform(user_input[:5].reshape(1,-1))

    prediction = np.round(model.predict(user_input.reshape(1,-1)),2)

    return render_template('Price_result.html',prediction=prediction[0])




@app.errorhandler(404)
def error(e):
    return render_template("error.html"),404

############################### EXECUTING THE APP ##################################


if __name__ == '__main__':
    app.run(debug=True)
