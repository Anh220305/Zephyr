# data_analyzer.py
import pandas as pd
from config import API_KEY

class DataSpecialist:
    def __init__(self, data):
        self.data = data
        self.api_key = API_KEY

    def analyze_data(self):
        # Check for missing values
        missing_data = self.data.isnull().sum()
        
        # Descriptive statistics
        description = self.data.describe()

        # Identify categorical features
        categorical_data = self.data.select_dtypes(include=['object']).nunique()

        # Potential anomalies (outliers or missing data)
        anomalies = self.find_anomalies()

        analysis_report = {
            "missing_data": missing_data.to_dict(),
            "description": description.to_dict(),
            "categorical_data": categorical_data.to_dict(),
            "anomalies": anomalies
        }

        return analysis_report

    def find_anomalies(self):
        anomalies = {}
        for col in self.data.select_dtypes(include=[float, int]):
            lower = self.data[col].quantile(0.25)
            upper = self.data[col].quantile(0.75)
            iqr = upper - lower
            outliers = self.data[(self.data[col] < lower - 1.5 * iqr) | (self.data[col] > upper + 1.5 * iqr)]
            if not outliers.empty:
                anomalies[col] = outliers
        return anomalies.to_dict()

    def communicate_analysis(self, report_generator):
        analysis_report = self.analyze_data()
        report_generator.receive_analysis(analysis_report)
