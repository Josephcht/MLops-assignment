from flask import Flask, render_template,request,redirect,url_for, flash
from Forms import PredictionForm,MyForm
import pandas as pd
import pickle
import numpy as np
import pycaret
from datetime import datetime
from pycaret.regression import *
app = Flask(__name__)
loaded_best_pipeline = load_model('final_model_lightgbm')
cols = ['block', 'street_name', 'town', 'postal_code', 'month', 'flat_type',
       'storey_range', 'floor_area_sqm', 'flat_model', 'lease_commence_date','cbd_dist', 'min_dist_mrt']
model = load_model('201423L_MLOps_Final')
n_cols = ['age', 'gender', 'chest_pain', 'resting_BP', 'cholesterol', 'fasting_BS', 'resting_ECG',
        'max_HR', 'exercise_angina', 'old_peak', 'ST_slope']
preds = ''
@app.route('/',methods=['GET', 'POST'])
def home():
    predict_form = PredictionForm(request.form)
    return render_template('prediction.html',form=predict_form)


@app.route('/predict', methods=['POST'])
def predict():
    error = None
    predict_form = PredictionForm(request.form)
    if request.method == 'POST' and predict_form.validate():
        date = predict_form.month.data
        date = date.strftime("%Y-%m")
        int_features = [predict_form.block.data,predict_form.street_name.data.upper(),predict_form.town.data.upper(),predict_form.postal_code.data,
                        date,predict_form.flat_type.data,predict_form.storey_range.data,predict_form.floor_area_sqm.data,
                        predict_form.flat_model.data,predict_form.lease_commence_date.data,predict_form.cbd_dist.data,predict_form.min_dist_mrt.data]
        data_unseen = pd.DataFrame([int_features], columns=cols)
        print(data_unseen)
        predictions = predict_model(loaded_best_pipeline, data=data_unseen,round=2)
        predictions = int(predictions.prediction_label[0])
    return render_template('prediction.html', form=predict_form, pred=predictions)

@app.route('/pred', methods=['GET','POST'])
def pred():
    global preds
    prediction_form = MyForm(request.form)
    if request.method =='POST' and prediction_form.validate():
        int_features = [prediction_form.age.data, prediction_form.gender.data, prediction_form.chest_pain.data, prediction_form.resting_BP.data
                        , prediction_form.cholesterol.data, int(prediction_form.fasting_BS.data), prediction_form.resting_ECG.data, prediction_form.max_HR.data
                        , prediction_form.exercise_angina.data, prediction_form.old_peak.data, prediction_form.ST_slope.data]
        data_unseen = pd.DataFrame([int_features], columns=n_cols)
        prediction = predict_model(model, data=data_unseen)
        preds = prediction.prediction_label[0]
    return render_template('pred.html', form = prediction_form, preds=preds)


if __name__ == "__main__":
    app.run(debug=True)
