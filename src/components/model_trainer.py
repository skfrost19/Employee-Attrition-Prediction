from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
import sys
import os
import pickle
import pandas as pd


class ModelTrainer:
    def __init__(
        self, data: pd.DataFrame, target: str, enforce_save: bool = False
    ) -> None:
        """
        Constructor of ModelTrainer class
        Params:
            data: pd.DataFrame
            target: str
        """
        self.data = data
        self.target = target
        self.enforce_save = enforce_save
        self.model = RandomForestClassifier()
        self.save_path = os.path.join(os.getcwd(), "models")
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def split_data(self) -> None:
        """
        Split data into train and test
        """
        try:
            logging.info("Splitting data into train and test")
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                self.data.drop(self.target, axis=1),
                self.data[self.target],
                test_size=0.2,
                random_state=123,
            )
        except Exception as e:
            logging.error(f"Error in split_data: {e}")
            raise CustomException(e, sys)

    def train_model(self) -> None:
        """
        Train model
        Params:
            model: sklearn random forest model
        """
        try:
            logging.info("Training model")
            self.model = self.model.fit(self.X_train, self.y_train)
        except Exception as e:
            logging.error(f"Error in train_model: {e}")
            raise CustomException(e, sys)

    def evaluate_model(self) -> None:
        """
        Evaluate model
        """
        try:
            logging.info("Evaluating model")
            y_pred = self.model.predict(self.X_test)
            print(f"Accuracy score: {accuracy_score(self.y_test, y_pred)}")
            print(f"Confusion matrix: {confusion_matrix(self.y_test, y_pred)}")
            print(
                f"Classification report: {classification_report(self.y_test, y_pred)}"
            )
        except Exception as e:
            logging.error(f"Error in evaluate_model: {e}")
            raise CustomException(e, sys)

    def save_model(self) -> None:
        """
        Save model
        """
        try:
            logging.info("Saving model")
            if self.enforce_save:
                if os.path.exists(self.save_path):
                    os.remove(self.save_path)
            if not os.path.exists(self.save_path):
                os.makedirs(self.save_path)
            pickle.dump(
                self.model, open(os.path.join(self.save_path, "model.pkl"), "wb")
            )
        except Exception as e:
            logging.error(f"Error in save_model: {e}")
            raise CustomException(e, sys)

    def run(self, model) -> None:
        """
        Run model training
        Params:
            model: sklearn model
        """
        try:
            logging.info("Running model training")
            self.split_data()
            self.train_model(model)
            self.evaluate_model()
            self.save_model()
        except Exception as e:
            logging.error(f"Error in run: {e}")
            raise CustomException(e, sys)
