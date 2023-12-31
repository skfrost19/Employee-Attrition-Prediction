import pandas as pd
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import standarize_data, categorical_to_numerical
from sklearn.utils import resample

sys.path.append(".")


class DataTransformation:
    def __init__(self, target: str, data_path: str) -> None:
        """
        Constructor
        """
        self.data_path = data_path
        self.target = target

    def load_data(self) -> pd.DataFrame:
        """
        Load data from csv
        Params:
                None
        Return:
                pd.DataFrame
        """
        try:
            logging.info("Loading data")
            df = pd.read_csv(self.data_path)
            return df
        except Exception as e:
            logging.error(f"Error in load_data: {e}")
            raise CustomException(e, sys)

    def drop_unwanted_columns(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Drop unwanted columns
        Params:
                data: pd.DataFrame
        Return:
                pd.DataFrame
        """
        try:
            logging.info("Dropping unwanted columns")
            data = data.drop(
                [
                    "HourlyRate",
                    "PercentSalaryHike",
                    "MonthlyRate",
                    "PerformanceRating",
                    "EducationField",
                    "EmployeeNumber",
                    "Over18",
                    "StandardHours",
                    "Education",
                    "Gender",
                ],
                axis=1,
            )
            return data
        except Exception as e:
            logging.error(f"Error in drop_unwanted_columns: {e}")
            raise CustomException(e, sys)

    def upsample_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Upsample data
        Params:
                data: pd.DataFrame
        Return:
                pd.DataFrame
        """
        try:
            logging.info("Upsampling data")
            df_majority = data[data[self.target] == 0]
            df_minority = data[data[self.target] == 1]
            df_minority_upsampled = resample(
                df_minority,
                replace=True,
                n_samples=df_majority.shape[0],
                random_state=42,
            )
            df_upsampled = pd.concat([df_majority, df_minority_upsampled])
            return df_upsampled

        except Exception as e:
            logging.error(f"Error in upsample_data: {e}")
            raise CustomException(e, sys)

    def run(self) -> pd.DataFrame:
        """
        Run data transformation
        Params:
                None
        Return:
                np.ndarray
        """
        try:
            logging.info("Running data transformation")
            data = self.load_data()
            data = self.drop_unwanted_columns(data)
            logging.info("Converting categorical columns to numerical")
            data = categorical_to_numerical(data)
            data = self.upsample_data(data)
            logging.info("Standarizing data")
            data = standarize_data(data, self.target)
            return data
        except Exception as e:
            logging.error(f"Error in run: {e}")
            raise CustomException(e, sys)
