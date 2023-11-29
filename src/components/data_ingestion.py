import os
import urllib.request
import sys
from src.exception import CustomException
from src.logger import logging


def data_ingestion():
    """Download data from GitHub repository and save it in the data folder
    Params:
            None
    Return:
            None
    """

    url = "https://raw.githubusercontent.com/IBM/employee-attrition-aif360/master/data/emp_attrition.csv"
    folder_name = "data"

    os.makedirs(folder_name, exist_ok=True)

    # Check if data has already been downloaded
    if os.path.isfile(os.path.join(folder_name, "employee_attrition.csv")):
        logging.info("Data already downloaded!")
        return

    try:
        logging.info("Downloading data...")
        urllib.request.urlretrieve(
            url, os.path.join(folder_name, "employee_attrition.csv")
        )
        logging.info("Data downloaded successfully!")

    except Exception as e:
        logging.error(f"Error downloading data: {e}")
        raise CustomException(e, sys)
