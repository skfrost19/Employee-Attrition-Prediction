from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import sys
from sklearn.preprocessing import LabelEncoder

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
        data = data.drop(target, axis=1)
        columns = data.columns - [target]
        scaler = StandardScaler()
        data = scaler.fit_transform(data)
        data = np.concatenate((data, np.array(data[target]).reshape(-1,1)), axis=1)
        data = pd.DataFrame(data, columns=columns+[target])
        return data
    except Exception as e:
        logging.error(f"Error in standarize_data: {e}")
        raise CustomException(e, sys)




def categorical_to_numerical(data: pd.DataFrame, target: str) -> pd.DataFrame:
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
        lf = LabelEncoder()
        df_new = data.copy()
        for col in df_new.columns:
            if df_new[col].dtype == "object":
                df_new[col] = lf.fit_transform(df_new[col])
        return df_new
    except Exception as e:
        logging.error(f"Error in categorical_to_numerical: {e}")
        raise CustomException(e, sys)