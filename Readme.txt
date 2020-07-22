FLIGHT FARE PREDICTOR: Project Overview

 * Created a tool that predicts flight fare (MAE ~ Rs.1184) to help people to a make 
   fare prediction for their flight.
 * The dataset is taken from Kaggle "Flight Fare Prediction Dataset by MachineHack".
 * Features like date and time of journey have been extracted in proper format.
 * Used ExtraTreeRegressor for feature selection. Optimized RandomForestRegressor
   using RandomizedSearchCV to get the best parameters for to build model.
 * Built a client facing API using Flask

RESOURCES
 
 * Webpage backhground image source-"https://images.unsplash.com/photo-1464037866556-6812c9d1c72e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80".
 * Dataset source- "("https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh/")."
 * A special thanks to Krish naik ("https://www.linkedin.com/in/naikkrish/") and Amar Mandal ("https://www.linkedin.com/in/amar-mandal/") for sharing thier knowledge  and idea of the       project.

DATA CLEANING

 * Parsed the date, month and year of journey separately.
 * Parsed the time of arrival and departure. 
 * Made a separate columns for hour and minute for arrival and departure.
 * Sorted the data in of flight duration in proper format ( H M). And parsed the hour and minute separately
 * Dropped the rows with missing data.
 * Used one-hot-endcoding to handle the categorical features.
 * Dropped the column Additional_Info as larger percent of data in it was "No-Info".
 * Droppped Route as it was representing the iformation similar to column  Total_stops.
 * Simplified the column Total_stops.

EDA

 * Used heatmap to find the correlation.
 * Also used the boxplot.

MODEL BUILDING

 * ExtraTreeRegressor is used to find the important features i.e. for feature selection.
 * Baseline Model - RandomForestRegressor
 * RandomForestRegressor with best parmeters is used after doing a RandomizedSearchCV on the baseline model.
 * Used pickel to save the model.

MODEL PERFORMANCE

 * MAE = 1183.4 
 * R^2 score = 0.82

DEPLOYMENT

 Built a Flask API endpoint that was hosted on a local webserver. The API endpoint takes the list of values and return the predicted fare price

MOTIVATION
 The whole purpose of doing this project is to learn th Data Science and Machine Learning and to get the hands on experience in order to get ready for the industry.

FUTURE SCOPE 

 * Real time scrapper and data processing code can be used to collect the data and train the model on that data for more accurate perditions.
 * More effficient feature engineering is possible with categorical features.
 * Different algorithm can be used to improve the accuracy.