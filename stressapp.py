import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open("F:\\Desktop\\stress app\\trained_model.sav",'rb'))

# Creating a function for stress prediction
def stress_prediction(input_data):
    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_as_numpy_array = input_data_as_numpy_array.astype(np.float64)
    # Reshape the array as we are predicting for one instance
    input_data_reshaped = [input_data_as_numpy_array]

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The person is not stressed'
    elif prediction[0] == 1:
        return 'The person is slightly stressed'
    elif prediction[0] == 2:
        return 'The person is stressed'
    elif prediction[0] == 3:
        return 'The person is highly stressed'

# Main function for Streamlit app
def main():
    # Styling the title with a colorful and stylish design
    st.markdown("""
        <style>
            h2 {
                color: #ffffff;
                text-align: center;
                padding: 15px;
                background: linear-gradient(45deg, #FF7E5F, #FF69B4);
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                transition: transform 0.2s ease-in-out;
            }
            h2:hover {
                transform: scale(1.05);
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<h2>Stress Level Predictor</h2>", unsafe_allow_html=True)

    # Getting the input data from the user
    body_temperature = st.text_input('Body temperature')
    limb_movement = st.text_input('Limb movement')
    blood_oxygen = st.text_input('Blood oxygen')
    sleeping_hours = st.text_input('Sleeping hours')
    heart_rate = st.text_input('Heart rate')

    # Code for prediction
    diagnosis = ''

    # Creating a button for prediction
    if st.button('Predict Stress'):
        diagnosis = stress_prediction([body_temperature, limb_movement, blood_oxygen, sleeping_hours, heart_rate])

    # Styling the result with a colorful and stylish design
    st.markdown("""
        <style>
            .result {
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                background: linear-gradient(45deg, #00FF7F, #00BFFF);
                color: #ffffff;
                text-align: center;
                transition: transform 0.2s ease-in-out;
            }
            .result:hover {
                transform: scale(1.05);
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown(f"<div class='result'>{diagnosis}</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()


    ###################################################################################


