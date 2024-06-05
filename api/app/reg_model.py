import os 
from tensorflow import keras
import numpy as np
import pandas as pd
#get os parent dir
dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(dir, os.pardir))
target_dir = os.path.join(parent_dir, 'app/static/models')

regression_path = os.path.join(target_dir, '1dconv_reg.h5')

def regression_model(data):
    model = keras.models.load_model(regression_path)
    predictions = model.predict(data)

    pred = [float(x) for x in predictions]
    return pred
