from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    CRIM : float
    ZN : float
    INDUS : float
    CHAS : int
    NOX : float
    RM : float
    AGE : float
    DIS : float
    RAD : int
    TAX : float
    PTRATIO : float
    B : float
    LSTAT : float

# loading the saved model
house_price_model = pickle.load(open('house_price_model.sav','rb'))

@app.post('/house_price_prediction')
def house_price_predd(input_parameter : model_input):

    input_data = input_parameter.json()
    input_dictionary = json.loads(input_data)

    crim = input_dictionary['CRIM']
    zn = input_dictionary['ZN']
    indus = input_dictionary['INDUS']
    chas = input_dictionary['CHAS']
    nox = input_dictionary['NOX']
    rm = input_dictionary['RM']
    age = input_dictionary['AGE']
    dis = input_dictionary['DIS']
    rad = input_dictionary['RAD']
    tax = input_dictionary['TAX']
    ptratio = input_dictionary['PTRATIO']
    b = input_dictionary['B']
    lstat = input_dictionary['LSTAT']

    input_list = [crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]

    prediction = house_price_model.predict(input_list)
    return prediction