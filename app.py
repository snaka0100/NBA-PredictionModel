from flask import Flask, request, url_for, render_template, redirect, jsonify
import pandas as pd
import tensorflow
import joblib
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
from sklearn.svm import SVC 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
RFmodel = joblib.load("Random_Forest_Model.sav")
SVMmodel = joblib.load("SVM_Model.sav")
DLmodel = keras.models.load_model("Deep_Learning_Model.h5")

app = Flask(__name__)


@app.route("/")
def index():
    #Home page
    return render_template("index.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route('/predictinput', methods = ['POST'])
def predictinput():
    features = [x for x in request.form.values()]
    pred = features[0]
    model_used = features[-1]
    return render_template('predict.html',prediction='Expected PER will be {} using {}'.format(pred, model_used))

@app.route("/overview")
def overview():
    return render_template("overview.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/model")
def model():
    return render_template("modelOverview.html")

@app.route("/NBAData")
def NBAData():
    df = pd.read_csv("https://uci-dataproject3.s3-us-west-1.amazonaws.com/AllTimeNbaSeason4Categories1990.csv")
    json_data = df.to_json(orient="records")
    return json_data

if __name__ == "__main__":
    app.run(debug=True)