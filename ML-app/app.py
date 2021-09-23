#import dependencies
from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
from urllib.request import urlopen 
import json


# create an instance of Flask
app = Flask(__name__)

# create the index route
@app.route('/')
def home():
    return render_template('index.html')

# intialize forecaste data array
# make this a global variable so that we can access it in other routes without hitting the api again
forecast_data = []

# access the api that delivers faux weather forecast data
# forecaste of the predictors in ML model were not available for free so this is only mock data
@app.route('/import')
def imprt():
    with urlopen('https://enestvedtforecast.herokuapp.com/forecast2') as r:
        text = r.read()
    jsonResponse = json.loads(text.decode('utf-8'))
    # access and writed to the global forecast_data array
    global forecast_data 
    forecast_data = jsonResponse
    return text


# this route feeds "forecast_data" to the ML model api and returns an watts per hour output forecast
@app.route('/predict2')
def background_process():
    # array to hold hourly output values
    predicted_output = []
    
    print(forecast_data)
    # open ML file
    file = open("pe_trained_linear.pickle","rb")

    # load trained model
    trained_model = pickle.load(file)

    # loop each hour / apply model / push result to array
    for row in forecast_data:
        myData = row
        print(myData['ALLSKY_SFC_SW_DWN'])
        #place all values in array
        test_data = [myData['month'], myData["hour"], myData["ALLSKY_SFC_SW_DWN"], myData["T2M"], myData["RH2M"]]
        print(test_data)
        
        #convert value data into numpy array
        test_data = np.array(test_data)
        
        #reshape array
        test_data = test_data.reshape(1,-1)
        print(test_data)
    
        #predict
        prediction = trained_model.predict(test_data)
        print(prediction[0][0])
        return_prediction = prediction[0][0]
        if return_prediction < 0:
            return_prediction = 0
        
        #append row to "predicted_output"
        predicted_output.append({myData["hour"]: return_prediction})
        print(predicted_output)
    print(predicted_output)
    
    # return list of dictionaries containing hourly predictions
    return jsonify(result = predicted_output)


if __name__ == '__main__':
    app.run(debug=True)