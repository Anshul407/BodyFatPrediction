import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
model = pickle.load('model.sav')

# Function to predict body fat
def predict_body_fat(data):
    return model.predict(data)

# Main function for Streamlit app
def main():
    # Title
    st.title('Body Fat Prediction App')

    # Input fields
    density = st.number_input('Density', format="%.4f")
    age = st.slider('Age', 18, 100, 30)
    weight = st.number_input('Weight (kg)', min_value=30.0, max_value=200.0, step=0.1)
    height = st.number_input('Height (cm)', min_value=100.0, max_value=250.0, step=0.1)
    neck = st.number_input('Neck Circumference (cm)', min_value=20.0, max_value=50.0, step=0.1)
    chest = st.number_input('Chest Circumference (cm)', min_value=50.0, max_value=150.0, step=0.1)
    abdomen = st.number_input('Abdomen Circumference (cm)', min_value=50.0, max_value=150.0, step=0.1)
    hip = st.number_input('Hip Circumference (cm)', min_value=50.0, max_value=150.0, step=0.1)
    thigh = st.number_input('Thigh Circumference (cm)', min_value=20.0, max_value=100.0, step=0.1)
    knee = st.number_input('Knee Circumference (cm)', min_value=20.0, max_value=50.0, step=0.1)
    ankle = st.number_input('Ankle Circumference (cm)', min_value=15.0, max_value=35.0, step=0.1)
    biceps = st.number_input('Biceps Circumference (cm)', min_value=20.0, max_value=60.0, step=0.1)
    forearm = st.number_input('Forearm Circumference (cm)', min_value=15.0, max_value=40.0, step=0.1)
    wrist = st.number_input('Wrist Circumference (cm)', min_value=10.0, max_value=30.0, step=0.1)

    # Prepare input data as DataFrame
    data = {
        'Density': density,
        'Age': age,
        'Weight': weight,
        'Height': height,
        'Neck': neck,
        'Chest': chest,
        'Abdomen': abdomen,
        'Hip': hip,
        'Thigh': thigh,
        'Knee': knee,
        'Ankle': ankle,
        'Biceps': biceps,
        'Forearm': forearm,
        'Wrist': wrist
    }
    
    # Create a DataFrame from the input data
    data_df = pd.DataFrame(data, index=[0])

    if st.button('Predict'):
        prediction = predict_body_fat(data_df.values)
        # Customize the output based on your model's prediction
        st.success(f'Predicted Body Fat Percentage: {prediction[0]:.2f}%')

# Run the app
if __name__ == '__main__':
    main()
