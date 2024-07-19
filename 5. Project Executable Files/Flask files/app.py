from flask import Flask, render_template, request
import joblib
import pickle
import numpy as np
from tensorflow.keras.models import load_model
ct = joblib.load("modelle")
sc = pickle.load(open("modelscaler.pkl","rb"))
model = load_model("model.h5")
app = Flask(__name__)
@app.route('/')
def loadpage():
    return render_template("index.html")

@app.route('/y_predict', methods = ["POST"])
def prediction():
    
    ID = request.form["ID"]
    WarehouseBlock = request.form["Warehouse Block"]
    ModeOfShipment = request.form["Mode Of Shipment"]
    CustomerCalls = request.form["Calls"]
    CustomerRating = request.form["Rating"]
    Cost = request.form["Cost"]
    PriorPurchase = request.form["Prior Purchase"]
    ProductImportance = request.form["Product Importance"]
    Gender = request.form["Gender"]
    Discount = request.form["Discount"]
    Weight = request.form["Weight"]
    x_test = [[float(Discount),CustomerCalls,Gender,float(Cost),float(Weight),ID,WarehouseBlock,CustomerRating,ProductImportance,ModeOfShipment]]
    print(x_test)
    
    p = np.array(scaler.transform(le.transform(x_test)))
    p = p.astype(np.float32)
    
    prediction = model.predict(p)
    
    prediction = prediction > 0.5
    
    if (prediction == [[False]]):
        text = "The Product will not reach on time."
    else:
        text = "The Product will reach on time."
        
   
    return render_template("index.html",prediction_text = text )

    
    
if __name__ == "__main__":
    app.run(debug = True)
