from src.components.predict import predict
from src.components.pipeline import pipeline
from src.components.predict import predict


if __name__ == "__main__":
    pipeline()
    # Must be in this order
    params = {
        "Age": 53,
        "BusinessTravel": "Travel_Rarely",
        "DailyRate": 1182,
        "Department": "Research & Development",
        "DistanceFromHome": 2,
        "EmployeeCount": 1,
        "EnvironmentSatisfaction": 4,
        "JobInvolvement": 3,
        "JobLevel": 2,
        "JobRole": "Research Scientist",
        "JobSatisfaction": 4,
        "MaritalStatus": "Married",
        "MonthlyIncome": 15427,
        "NumCompaniesWorked": 1,
        "OverTime": "No",
        "RelationshipSatisfaction": 3,
        "StockOptionLevel": 0,
        "TotalWorkingYears": 32,
        "TrainingTimesLastYear": 2,
        "WorkLifeBalance": 3,
        "YearsAtCompany": 5,
        "YearsInCurrentRole": 4,
        "YearsSinceLastPromotion": 1,
        "YearsWithCurrManager": 4,
    }
    print(predict(params))
