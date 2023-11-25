<<<<<<< Updated upstream
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
=======
# Employee Attrition Prediction

## Problem Statement

The objective of this project is to predict the employee attrition rate in organizations. The dataset contains various features such as employee satisfaction index, employee last evaluation, number of projects worked on, average monthly hours, time spent at the company, whether they have had a work accident, whether they have had a promotion in the last 5 years, departments they work for, salary level, etc. The dataset also contains the target column, i.e. whether they have left the organization or not. The dataset is imbalanced with the majority class being 0 (employees who have not left the organization). The dataset is available at https://raw.githubusercontent.com/IBM/employee-attrition-aif360/master/data/emp_attrition.csv

## Data Description

The dataset contains 1471 rows and 35 columns. The columns are described below:

1. Age: The age of the employee
2. Attrition: Whether the employee has left the company (Yes) or not (No)
3. BusinessTravel: The frequency of the employee's business travel
4. DailyRate: The employee's daily rate of pay
5. Department: The department the employee belongs to
6. DistanceFromHome: The distance between the employee's home and workplace
7. Education: The highest level of education completed by the employee
8. EducationField: The field of study of the employee's highest education
9. EmployeeCount: The number of employees in the company
10. EmployeeNumber: The unique identifier of the employee
11. EnvironmentSatisfaction: The employee's satisfaction with their work environment
12. Gender: The gender of the employee
13. HourlyRate: The employee's hourly rate of pay
14. JobInvolvement: The employee's level of involvement in their job
15. JobLevel: The level of the employee's job in the company hierarchy
16. JobRole: The employee's job role
17. JobSatisfaction: The employee's satisfaction with their job
18. MaritalStatus: The employee's marital status
19. MonthlyIncome: The employee's monthly income
20. MonthlyRate: The employee's monthly rate of pay
21. NumCompaniesWorked: The number of companies the employee has worked for prior to the current job
22. Over18: Whether the employee is over 18 years old (Yes)
23. OverTime: Whether the employee works overtime (Yes) or not (No)
24. PercentSalaryHike: The percentage of the employee's salary increase from the previous year
25. PerformanceRating: The employee's performance rating
26. RelationshipSatisfaction: The employee's satisfaction with their relationships at work
27. StandardHours: The standard number of working hours for the company
28. StockOptionLevel: The employee's level of stock options
29. TotalWorkingYears: The total number of years the employee has worked
30. TrainingTimesLastYear: The number of times the employee received training last year
31. WorkLifeBalance: The employee's satisfaction with their work-life balance
32. YearsAtCompany: The number of years the employee has worked at the company
33. YearsInCurrentRole: The number of years the employee has been in their current role
34. YearsSinceLastPromotion: The number of years since the employee's last promotion
35. YearsWithCurrManager: The number of years the employee has worked with their current manager

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
>>>>>>> Stashed changes
