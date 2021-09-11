from logging import debug
from flask import Flask, jsonify
import pandas as pd

 


app =Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://odbdvuvvbwaskm:3c8c221203003dffa9441f8d77e22b5ac42d577bb422fdfdd19f8997e69b8a0f@ec2-34-196-238-94.compute-1.amazonaws.com:5432/d6ka9b9eufj4l4"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
engine = create_engine("postgresql://odbdvuvvbwaskm:3c8c221203003dffa9441f8d77e22b5ac42d577bb422fdfdd19f8997e69b8a0f@ec2-34-196-238-94.compute-1.amazonaws.com:5432/d6ka9b9eufj4l4")


#################################################
@app.route("/")
def hello_world():
    return "it works"

@app.route("/forecast")
def forecast():
    data = [
        [0,1,2,3,4],
        [4,5,6,7,8]
    ]
    return jsonify(data)

@app.route("/forecast2")
def forecast2():
    # forecast_data = []
    # with engine.connect() as connection:
    #     result = connection.execute("select \"month\", \"hour\", \"ALLSKY_SFC_SW_DWN\", \"T2M\", \"RH2M\" from history where date(\"Time\") = date(now()- interval '364 day') order by \"hour\"")
    #     for row in result:
    #         daily_vals = {
    #             "month": row['month'],
    #             "hour": row['hour'],
    #             "ALLSKY_SFC_SW_DWN": row['ALLSKY_SFC_SW_DWN'],
    #             "T2M": row['T2M'],
    #             "RH2M": row['RH2M']
    #         }
    #         forecast_data.append(daily_vals)
            
    
    # return jsonify(forecast_data)

    my_record = pd.read_sql("select \"month\", \"hour\", \"ALLSKY_SFC_SW_DWN\", \"T2M\", \"RH2M\" from history where date(\"Time\") = date(now()- interval '364 day') order by \"hour\"", engine)
    
    print(my_record.columns)
    return my_record.to_json(orient="records")

if __name__ == "__main__":
    app.run(debug=True)

