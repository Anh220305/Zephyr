# report_generator.py
class ReportGenerator:
    def __init__(self):
        self.analysis_data = None

    def receive_analysis(self, analysis_report):
        self.analysis_data = analysis_report
        self.generate_report()

    def generate_report(self):
        if not self.analysis_data:
            print("No data to generate report.")
            return

        print("Analysis Report:")
        print("\nMissing Data:")
        for column, missing in self.analysis_data['missing_data'].items():
            print(f"{column}: {missing} missing entries")

        print("\nDescriptive Statistics:")
        for col, stats in self.analysis_data['description'].items():
            print(f"{col}: {stats}")

        print("\nCategorical Data Analysis:")
        for col, unique in self.analysis_data['categorical_data'].items():
            print(f"{col}: {unique} unique categories")

        print("\nAnomalies Detected:")
        for col, anomalies in self.analysis_data['anomalies'].items():
            print(f"{col} anomalies detected: {anomalies}")
