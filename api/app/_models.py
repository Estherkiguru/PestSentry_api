import os 
from tensorflow import keras
import numpy as np
import pandas as pd
#get os parent dir
dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(dir, os.pardir))
target_dir = os.path.join(parent_dir, 'app/static/models')

#model path
classification_path = os.path.join(target_dir, '1dcov_classification.h5')
regression_path = os.path.join(target_dir, '1dconv_reg.h5')

'''
model loading
postprocessing model results
'''
def classification_model(data):
    model = keras.models.load_model(classification_path)
    predictions = model.predict(data)
    predictions = np.argmax(predictions, axis=1)
    list = []

    for i in range(len(predictions)):
        if predictions[i] == 1:
            Labels = "Above_mrl_14x"
        
        elif predictions[i] == 2:
            Labels = "Above_mrl_17x"

        elif predictions[i] == 3:
            Labels = "Above_mrl_20x"

        elif predictions[i] == 4:
            Labels = "Above_mrl_23x"

        elif predictions[i] == 5:
            Labels = "Above_mrl_50x"

        elif predictions[i] == 6:
            Labels = "Above_mrl_29x"

        elif predictions[i] == 7:
            Labels = "Above_mrl_38x"

        elif predictions[i] == 8:
            Labels = "Above_mrl_94x"

        elif predictions[i] == 9:
            Labels = "Above_mrl_173x"

        elif predictions[i] == 10:
            Labels = "Above_mrl_191x"

        elif predictions[i] == 11:
            Labels = "Above_mrl_219x"

        else:
            Labels = "2ppm_or_below"

    # Append the data for each prediction
        list.append((Labels))
    return list



def regression_model(data):
    model = keras.models.load_model(regression_path)
    predictions = model.predict(data)

    pred = [float(x) for x in predictions]
    return pred

