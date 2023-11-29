import os
import sys
from src.components.data_ingestion import data_ingestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging
from src.exception import CustomException


def pipeline():
    """
    Executes all the stages of the machine learning pipeline
    Params:
            None
    Return:
            None
    """
    logging.info("Executing pipeline")
    try:
        data_ingestion()
        data_path = os.path.join(os.getcwd(), "data", "employee_attrition.csv")
        target = "Attrition"
        transformed_data = DataTransformation(target=target, data_path=data_path).run()
        ModelTrainer(data=transformed_data, target=target, enforce_save=True).run()
    except Exception as e:
        logging.error(f"Error in pipeline: {e}")
        raise CustomException(e, sys)
