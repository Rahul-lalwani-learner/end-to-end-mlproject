# This file is made for deployment purposes. 
from flask import Flask, request, render_template, redirect
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import PredictPipeline, CustomData


application = Flask(__name__) # initializing a flask app

app = application

## Route for a home page

@app.route('/', methods=['GET', 'POST'])
def index(): 
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint(): 
    if request.method == "GET": 
        return render_template('home.html')
    else: 
        data = CustomData(
            gender = request.form.get('gender'),
            race_ethnicity= request.form.get('race_ethnicity'),
            parental_level_of_education= request.form.get('parental_level_of_education'),
            lunch= request.form.get('lunch'),
            test_preparation_course= request.form.get('test_preparation_course'),
            reading_score= int(request.form.get('reading_score')),
            writing_score= int(request.form.get('writing_score'))
        ) # this will come from predict_pipeline.py in src.pipeline folder

        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template("home.html", results = results[0])
    
if __name__ == "__main__":
    # print("The server is running on {}".format("http://127.0.0.1:5000"))
    app.run(host="0.0.0.0")