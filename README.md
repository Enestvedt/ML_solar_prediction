Team: Paul, Pat and Greg

# ML_solar_prediction
Machine learning application that predicts five days of solar production based on weather forecast.

Use machine learning models to predict the solar energy production of a new photovoltaic array in Minneapolis, MN.

We will create a machine learning model that takes ‘features’ of weather (temperature, solar radiation, wind, air quality, etc.) and determines their effect on solar production of panels at that same location. The module will use 2.5 years of hourly weather data merged with 2.5 years of solar installation output data.  Data will be cleaned and merged in PANDAS.  The model will be developed with the SciKit Learn library.

The resulting model (Python application) will be made available via api on Heroku.  It will be a simple api that receives an x-day weather forecast and returns predicted panel production for those days.

We will create a website that displays static visualizations of weather and array outputs for the given 2.5 yr time period.  We will use Plotly and Tableau to create visualizations.  We will use D3 to generated the dynamic 5-day predicted output visualization.

This type of data, used at larger scale, could be used by energy companies to manage production and load on the electrical grid.  It could also be used in smart home applications such shifting the schedule non-essential electricity use or manage storage vs sale to grid (capitalizing on net-meter price vs purchase price).

Steps:
1. Merge Data / Pandas
2. Develop ML model in SciKit Learn / save the model.
3. Create Flask API (@route) for python model.
4. Load API to Heroku.
5. Create Static Visualizations of Weather and Solar Production Data using MatPlot and/or Tableau.
6. Access Open Weather API (or other) and retrieve 5-day forecast.  
7. Create Web site that displays static visualizations / access Open Weather API and feeds that to our Heroku Api and returns forecast of five-day solar production.
8. Host site on GitHub pages.


Data Sources): 
- NREL Database:  https://maps.nrel.gov/nsrdb-viewer/?aL=x8CI3i%255Bv%255D%3Dt%26Jea8x6%255Bv%255D%3Dt%26Jea8x6%255Bd%255D%3D1%26VRLt_G%255Bv%255D%3Dt%26VRLt_G%255Bd%255D%3D2%26mcQtmw%255Bv%255D%3Dt%26mcQtmw%255Bd%255D%3D3&bL=clight&cE=0&lR=0&mC=9.362352822055605%2C-23.027343749999996&zL=3
- Paul’s Neighbor provided a 2.5 year set of hour data production data from his residential array of 24 x 380W PV panels.

