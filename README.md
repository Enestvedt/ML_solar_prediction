# ML_solar_prediction
Machine learning application that predicts next day of solar production based on forecast.

Use machine learning models to predict the solar energy production of a new photovoltaic array in Minneapolis, MN.

We created a machine learning model that takes ‘features’ of weather available form NASA Power Project and determines their effect on solar production of panels at that same location. The module will use 2.5 years of hourly weather data merged with 2.5 years of solar installation output data.  Data was processed and merged using PANDAS.  The model was developed with the SciKit Learn library.

The resulting model (Python application) was made available via api on Heroku.  It will be a simple api that receives a faux conditions forecast from our own mock predictor API and returns predicted panel output value in Watts per hour. The mock predictor API returns conditions for today's date - 364 day.

We created a website that displays static visualizations of weather and array outputs for the given 2.5 yr time period.  We Tableau to create the visualizations. 

This type of data, used at larger scale, could be used by energy companies to manage production and load on the electrical grid.  It could also be used in smart home applications such shifting the schedule non-essential electricity use or manage storage vs sale to grid (capitalizing on net-meter price vs purchase price).

Steps:
1. Merge Data / Pandas
2. Develop ML model in SciKit Learn / save the model.
3. Create Flask API (@route) for python model.
4. Load API to Heroku.
5. Create Static Visualizations of Weather and Solar Production Data using MatPlot and/or Tableau.
6. Our goal was to use weather predictions to develop a model and predict future output.  Because we were not able to create a valid model using openly available weather data.  We opted to limit our project to the NASA data and create an api that serves a faux prediction of future conditions.  That mock data is used to produce an example prediction to represent what the model would return if the predictors were freely available.
7. Create Web site that displays static visualizations / create and access our own API and feeds a mock conditions forecast to our Heroku Api and returns forecast for the next day's energy production.
8. Host site on GitHub pages.


Data Sources): 
- The Power Project (NASA):  https://power.larc.nasa.gov/data-access-viewer/
- Paul’s Neighbor provided a 2.5 year set of hour data production data from his residential array of 24 x 380W PV panels.

