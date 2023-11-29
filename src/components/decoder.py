import os
import sys
import pickle
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException


def decoder(params: dict) -> pd.DataFrame:
    """
    Decodes the target variable for the given input
    Params:
            params: json
    Return:
            str
    """
    logging.info("Executing decoder")
    try:
        encoder_path = os.path.join(os.getcwd(), "encoders", "label_encoders.pkl")
        std_scaler_path = os.path.join(os.getcwd(), "encoders", "standard_scaler.pkl")
        with open(encoder_path, "rb") as f:
            encoders = pickle.load(f)
        with open(std_scaler_path, "rb") as f:
            std_scaler = pickle.load(f)
        data = pd.DataFrame(params, index=[0])

        # convert categorical columns to numerical
        for col in data.columns:
            if data[col].dtype == "object":
                data[col] = encoders[col].transform(data[col])

        # standarize data
        data = std_scaler.transform(data)

        data = pd.DataFrame(data, columns=list(params.keys()))
        return data

    except Exception as e:
        logging.error(f"Error in decoder: {e}")
        raise CustomException(e, sys)
