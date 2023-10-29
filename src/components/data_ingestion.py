import os
import urllib.request
import sys
from src.exception import CustomException
from src.logger import logging

url = "https://raw.githubusercontent.com/IBM/employee-attrition-aif360/master/data/emp_attrition.csv"
folder_name = "data"

if not os.path.exists(folder_name):
        os.makedirs(folder_name)

try:
        urllib.request.urlretrieve(url, os.path.join(folder_name, "data.csv"))
        logging.info("Data downloaded successfully!")
except Exception as e:
        logging.error(f"Error downloading data: {e}")
        raise CustomException(e,sys)

