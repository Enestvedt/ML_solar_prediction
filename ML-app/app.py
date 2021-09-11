#import Flask
from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
from urllib.request import urlopen 
import json


#create an instance of Flask
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict/', methods=['GET','POST'])
def predict():
    
    if request.method == "POST":
        
        #get form data
        month = request.form.get('month')
        hour = request.form.get('hour')
        ALLSKY_SFC_SW_DIFF = request.form.get('ALLSKY_SFC_SW_DIFF')
        T2M = request.form.get('T2M')
        RH2M = request.form.get('RH2M')

        
        #call preprocessDataAndPredict and pass inputs
        try:
            prediction = preprocessDataAndPredict(month, hour, ALLSKY_SFC_SW_DIFF, T2M, RH2M)
            #pass prediction to template
            return render_template('predict.html', prediction = prediction)
   
        except ValueError:
            return "Please Enter valid values"
  
        pass
    pass

def preprocessDataAndPredict(month, hour, ALLSKY_SFC_SW_DIFF, T2M, RH2M):
    
    #keep all inputs in array
    test_data = [month, hour, ALLSKY_SFC_SW_DIFF, T2M, RH2M]
    print(test_data)
    
    #convert value data into numpy array
    test_data = np.array(test_data)
    
    #reshape array
    test_data = test_data.reshape(1,-1)
    print(test_data)
    
    #open file
    file = open("pe_trained_linear.pickle","rb")

    #load trained model
    trained_model = pickle.load(file)
    
    #predict
    prediction = trained_model.predict(test_data)
    
    return prediction
    
    pass

forecast_data = []
@app.route('/import')
def imprt():
    with urlopen('https://enestvedtforecast.herokuapp.com/forecast2') as r:
        text = r.read()
    jsonResponse = json.loads(text.decode('utf-8'))
    global forecast_data
    forecast_data = jsonResponse
    return text


@app.route('/predict2')
def background_process():
    predicted_output = []
    
    print(forecast_data)
    # #open file
    file = open("pe_trained_linear.pickle","rb")

    # #load trained model
    trained_model = pickle.load(file)

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
        
        #pass prediction to template
        predicted_output.append({myData["hour"]: return_prediction})
        print(predicted_output)
    print(predicted_output)
    return jsonify(result = predicted_output)

    # return jsonify(result = [{"name": "Paul", "age": 10}, {"name": "Paul", "age": 10}])


if __name__ == '__main__':
    app.run(debug=True)