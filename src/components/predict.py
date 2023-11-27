import os
import sys
import pickle
import pandas as pd
from src.components.decoder import decoder
from src.logger import logging
from src.exception import CustomException


def predict(params: dict) -> str:
    """
    Predicts the target variable for the given input
    Params:
            params: json
    Return:
            str
    """
    logging.info("Executing predict")
    try:
        # decode the input
        data = decoder(params)
        model_path = os.path.join(os.getcwd(), "models", "model.pkl")
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        # predict
        prediction = model.predict(data)
        return "Yes" if prediction[0] == 1 else "No"

    except Exception as e:
        logging.error(f"Error in predict: {e}")
        raise CustomException(e, sys)
