import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('house_price_model.sav','rb'))

# creating a function for prediction
def house_price_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

def main():

    # giving a title
    st.title('House Price Prediction Web App')

    # getting the input data from the user
    CRIM = st.text_input('Per capita crime rate by town')
    ZN = st.text_input('Proportion of residential land zoned for lots over 25,000 sq. ft.')
    INDUS = st.text_input('Proportion of non-retail business acres per town')
    CHAS = st.text_input('Charles River dummy variable (1 if tract bounds river; 0 otherwise)')
    NOX = st.text_input('Nitric oxide concentration (parts per 10 million)')
    RM = st.text_input('Average number of rooms per dwelling')
    AGE = st.text_input('Proportion of owner-occupied units built prior to 1940')
    DIS = st.text_input('Weighted distances to five Boston employment centers')
    RAD = st.text_input('Index of accessibility to radial highways')
    TAX = st.text_input('Full-value property tax rate per $10,000')
    PTRATIO = st.text_input('Pupil-teacher ratio by town')
    B = st.text_input('1000*(Bk - 0.63)^2, where Bk is proportion of Black residents')
    LSTAT = st.text_input('Percentage of lower status population')

    # code for Prediction
    price = ''

    # creating button for prediction
    if st.button('House Price Result'):
        price = house_price_prediction([CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT])
        st.sucess(price)

if __name__=='__main__':

    main()
