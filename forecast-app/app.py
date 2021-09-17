from logging import debug
from flask import Flask, jsonify
import pandas as pd
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app =Flask(__name__)

#################################################
# Database Setup
#################################################


# SQLAlchemy 1.4.x has removed support for the postgres:// URI scheme, which is used by Heroku Postgres 
# replace with postgresql://
uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
engine = create_engine(uri)

#################################################
@app.route("/")
def hello_world():
    return "This api returns faux solar prediction values form 2020.  It is used to provide simulated values to a Machine Learning model to demonstrate a possible use case."


@app.route("/forecast2")
def forecast2():

    my_record = pd.read_sql("select \"month\", \"hour\", \"ALLSKY_SFC_SW_DWN\", \"T2M\", \"RH2M\" from history where date(\"Time\") = date(now()- interval '364 day') order by \"hour\"", engine)
    
    print(my_record.columns)
    return my_record.to_json(orient="records")

if __name__ == "__main__":
    app.run(debug=True)