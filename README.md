# Employee Attrition Prediction

## Problem Statement

The objective of this project is to predict the employee attrition rate in organizations. The dataset contains various features such as employee satisfaction index, employee last evaluation, number of projects worked on, average monthly hours, time spent at the company, whether they have had a work accident, whether they have had a promotion in the last 5 years, departments they work for, salary level, etc. The dataset also contains the target column, i.e. whether they have left the organization or not. The dataset is imbalanced with the majority class being 0 (employees who have not left the organization). The dataset is available at https://www.kaggle.com/ludobenistant/hr-analytics.

## Data Description

The dataset contains 14999 rows and 10 columns. The columns are described below:

1. satisfaction_level: Employee satisfaction level
2. last_evaluation: Last evaluation
3. number_project: Number of projects
4. average_montly_hours: Average monthly hours
5. time_spend_company: Time spent at the company
6. Work_accident: Whether they have had a work accident
7. left: Whether the employee has left
8. promotion_last_5years: Whether the employee was promoted in the last five years
9. sales: Department they work for
10. salary: Salary level

## Data Preprocessing

The dataset is imbalanced with the majority class being 0 (employees who have not left the organization). The dataset is split into train and test sets with a test size of 0.2. The train set is further split into train and validation sets with a validation size of 0.2. The categorical columns are one-hot encoded. The numerical columns are scaled using the StandardScaler. The target column is encoded using the LabelEncoder.

## Model Building

The following models are built:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. XGBoost
5. LightGBM

## Model Evaluation

The models are evaluated using the following metrics:

1. Accuracy
2. Precision
3. Recall
4. F1 Score
5. ROC AUC Score

## Results

The results are summarized below:

| Model               | Accuracy | Precision | Recall | F1 Score | ROC AUC Score |
| ------------------- | -------- | --------- | ------ | -------- | ------------- |
| Logistic Regression | 0.78     | 0.49      | 0.24   | 0.32     | 0.61          |
| Decision Tree       | 0.97     | 0.93      | 0.92   | 0.92     | 0.96          |
| Random Forest       | 0.99     | 0.99      | 0.97   | 0.98     | 0.99          |
| XGBoost             | 0.99     | 0.99      | 0.97   | 0.98     | 0.99          |
| LightGBM            | 0.99     | 0.99      | 0.97   | 0.98     | 0.99          |
