from flask import Flask, request, render_template
import pandas as pd    
import pickle

app = Flask(__name__)
model=pickle.load(open("flight.pkl","rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/about.html")
@cross_origin()
def about():
    return render_template("about.html")

@app.route("/home.html")
@cross_origin()
def return_home():
    return render_template("home.html")

@app.route("/predict", methods = ['GET','POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        #Journey Date
        dep_date = request.form["Dep_Time"]   
        dep_day = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").day)
        dep_month = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").month)
        dep_year = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").year)

        #Journey time
        dep_hour = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").hour)
        dep_minute = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").minute)

        #Arrival Time
        arrival_date = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(arrival_date, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(arrival_date, format ="%Y-%m-%dT%H:%M").minute)

        #Duration of flight

        duration_hour = Arrival_hour - dep_hour
        duration_minute = Arrival_min - dep_minute

        #Total Stops
        Total_stops = int(request.form["stops"])

        #Airline
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
        airline = request.form["airline"]

        if(airline =='Jet Airways'):
            Jet_Airways = 1
        elif (airline == 'IndiGo'):
            IndiGo = 1
        elif (airline == 'Air_India'):
            Air_India = 1
        elif (airline == 'Multiple_carriers'):
            Multiple_carriers = 1
        elif (airline == 'SpiceJet'):
            SpiceJet = 1
        elif (airline == 'Vistara'):
            Vistara = 1
        elif (airline == 'GoAir'):
            GoAir = 1
        elif (airline == 'Multiple_carriers_Premium_economy'):
            Multiple_carriers_Premium_economy = 1
        elif (airline == 'Jet_Airways_Business'):
            Jet_Airways_Business = 1
        elif (airline == 'Vistara_Premium_economy'):
            Vistara_Premium_economy = 1
        elif (airline == 'Trujet'):
            Trujet = 1

        #Source
        Delhi = 0
        Kolkata = 0
        Mumbai = 0
        Chennai = 0
        Source = request.form["Source"]

        if (Source == 'Delhi'):
            Delhi = 1
        elif (Source == 'Kolkata' ):
            Kolkata = 1
        elif (Source == 'Mumbai' ):
            Mumbai = 1
        elif (Source == 'Chennai' ):
            Chennai = 1
        
        #Destiantion
        Cochin = 0
        Delhi = 0
        New_Delhi = 0
        Hyderabad = 0
        Kolkata = 0
        dest=request.form["Destination"]
        if (dest == 'Cochin'):
            Cochin = 1
        elif (dest == 'Delhi'):
            Delhi = 1
        elif (dest == 'New_Delhi'):
            New_Delhi = 1
        elif (dest == 'Hyderabad'):
            Hyderabad = 1
        elif (dest == 'Kolkata'):
            Kolkata = 1

        prediction=model.predict([[
            Total_stops,
            dep_day,
            dep_month,
            dep_year,
            dep_hour,
            dep_minute,
            Arrival_hour,
            Arrival_min,
            duration_hour,
            duration_minute,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            Chennai,
            Delhi,
            Kolkata,
            Mumbai,
            Cochin,
            Delhi,
            Hyderabad,
            Kolkata,
            New_Delhi
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
