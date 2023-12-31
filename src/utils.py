from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import sys
from sklearn.preprocessing import LabelEncoder
import os
import pickle


def standarize_data(data: pd.DataFrame, target: str) -> pd.DataFrame:
    """
    Standarize data using StandardScaler
    Params:
        data: pd.DataFrame
        target: str
    Return:
        np.ndarray
    """

    try:
        logging.info("Standarizing data")
        # save columns in list
        columns = list(data.columns)
        columns.remove(target)
        target_data = data[target]
        data = data.drop(target, axis=1)
        scaler = StandardScaler()
        data = scaler.fit_transform(data)

        # save the scaler (create a folder named encoders if not present)
        os.makedirs("encoders", exist_ok=True)
        with open("encoders/standard_scaler.pkl", "wb") as f:
            pickle.dump(scaler, f)

        data = np.concatenate((data, np.array(target_data).reshape(-1, 1)), axis=1)
        data = pd.DataFrame(data, columns=columns + [target])
        return data
    except Exception as e:
        logging.error(f"Error in standarize_data: {e}")
        raise CustomException(e, sys)


def categorical_to_numerical(data: pd.DataFrame) -> pd.DataFrame:
    """
    Convert categorical columns to numerical
    Params:
        data: pd.DataFrame
        target: str
    Return:
        pd.DataFrame
    """
    try:
        logging.info("Converting categorical columns to numerical")
        df_new = data.copy(deep=True)
        encoders = {}

        for col in df_new.columns:
            if df_new[col].dtype == "object":
                lf = LabelEncoder()
                df_new[col] = lf.fit_transform(df_new[col])
                encoders[col] = lf

        # save the encoders (create a folder named encoders if not present)
        os.makedirs("encoders", exist_ok=True)
        with open("encoders/label_encoders.pkl", "wb") as f:
            pickle.dump(encoders, f)

        return df_new
    except Exception as e:
        logging.error(f"Error in categorical_to_numerical: {e}")
        raise CustomException(e, sys)
