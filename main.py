from src.components.predict import predict
from src.components.pipeline import pipeline
from src.components.predict import predict


if __name__ == "__main__":
    pipeline()
    # Must be in this order
    params = {
        "Age": 41,
        "BusinessTravel": "Travel_Rarely",
        "DailyRate": 1102,
        "Department": "Sales",
        "DistanceFromHome": 1,
        "EmployeeCount": 1,
        "EnvironmentSatisfaction": 2,
        "JobInvolvement": 3,
        "JobLevel": 2,
        "JobRole": "Sales Executive",
        "JobSatisfaction": 4,
        "MaritalStatus": "Single",
        "MonthlyIncome": 5993,
        "NumCompaniesWorked": 8,
        "OverTime": "Yes",
        "RelationshipSatisfaction": 1,
        "StockOptionLevel": 0,
        "TotalWorkingYears": 8,
        "TrainingTimesLastYear": 0,
        "WorkLifeBalance": 1,
        "YearsAtCompany": 6,
        "YearsInCurrentRole": 4,
        "YearsSinceLastPromotion": 0,
        "YearsWithCurrManager": 5,
    }
    print(predict(params))
