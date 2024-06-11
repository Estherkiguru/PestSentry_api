import os 
from tensorflow import keras
import numpy as np
import pandas as pd
#get os parent dir
dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(dir, os.pardir))
target_dir = os.path.join(parent_dir, 'app/static/models')


# Model path for regression
regression_path = os.path.join(target_dir, '1dconv_reg.h5')

# Function to perform regression using a pre-trained model
def regression_model(data):
    # Load the pre-trained regression model
    model = keras.models.load_model(regression_path)
    
    # Make predictions using the model
    predictions = model.predict(data)

    # Convert predictions to list of floats
    pred = [float(x) for x in predictions]
    return pred
