# Create API of ML model using flask

# Importing necessary modules
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import pandas as pd


app = Flask(__name__)

# To make sure our URL work properly
@app.route('/')
def hello():
    return 'heelo USER!'

# Load the Model
model = joblib.load('/home/andreasmm/mysite/random forrest.pkl')

# Creating url /api
@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # If our data only consist of one observation, it directly convert it into DataFrame with one observation
    if type(data['limit'])!=list:
        d=pd.DataFrame([data])

    # If our data has more than one, to make it correctly converted to data frame, we use below code instead
    else:
        d=pd.DataFrame({"limit":data['limit'],"age":data['age'],"bill":data['bill']}) # If we directly convert to dataframe, it will only consist of one obs with each column is a list of corresponding column.
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict(d)

    # Take the value of prediction into strings
    a=[]
    for val in prediction:
        if val==1:
            a.append("Hasil Predksi : "+str(val) + ", Sehingga diprediksi pembayaran Terlambat")
        else:
            a.append("Hasil Prediksi : "+str(val) + ", Sehingga diprediksi pembayaran Tidak terlambat")


    return jsonify(a)
