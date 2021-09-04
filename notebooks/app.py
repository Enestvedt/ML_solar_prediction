# Import Dependencies
from flask import Flask, jsonify
# Note: these next 3 imports are just needed to generate MSE and r2 
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd 

# API definition
app = Flask(__name__)

@app.route('/')
def welcome():
    return (
        f"Welcome to our initial ML Interface v1.0!<br/>"
        f"Try using the following path:<br/>"
        f"127.0.0.1:5000/predict"
        )

@app.route('/predict')
def predict():
    # Note - for test purposes, just using a subset of our test file and removing the -999s.    
    consolidated_data = pd.read_csv("../csv_downloads/merged_data_subset.csv")
    clean_consolidated_data = consolidated_data[~consolidated_data.eq(-999).any(1)]

    data2 = clean_consolidated_data[['ALLSKY_SFC_SW_DWN',
           'ALLSKY_KT',
           'ALLSKY_SRF_ALB',
           'SZA',
           'ALLSKY_SFC_PAR_TOT',
           'ALLSKY_SFC_UVA',
           'ALLSKY_SFC_UVB',
           'ALLSKY_SFC_UV_INDEX',
           'T2M',
           'RH2M',
           'PS',
           'WD10M']]
    y = clean_consolidated_data['Energy (Wh)'].values.reshape(-1, 1)
    
    # Loading the previously stored model
    loaded_model = joblib.load('model.pkl')
    
    # The following is needed to arrive at the MSE and r2 to be able to return and display the values back to the UI
    X_train, X_test, y_train, y_test = train_test_split(data2, y, random_state=42)
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)

    predictions = loaded_model.predict(X_test_scaled)
    loaded_model.fit(X_train_scaled, y_train_scaled)
    
    # These were chosen to quickly return values for this initial Flask.  
    MSE = mean_squared_error(y_test_scaled, predictions)
    r2 = loaded_model.score(X_test_scaled, y_test_scaled)
    
    # Return these back and display on the screen.  
    return jsonify({'MSE': str(MSE)}, {'r2': str(r2)})

if __name__ == '__main__':
    app.run(debug=True)