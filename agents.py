# agent.py
from data_analyzer import DataSpecialist
from report_generator import ReportGenerator

class AIAgent:
    def __init__(self, data):
        self.data_specialist = DataSpecialist(data)
        self.report_generator = ReportGenerator()

    def run(self):
        print("Data Specialist analyzing the data...")
        self.data_specialist.communicate_analysis(self.report_generator)
