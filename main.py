# main.py
import pandas as pd
from agent import AIAgent

# Load data
data = pd.read_csv('data.csv')

# Initialize AI agents
ai_agent = AIAgent(data)

# Run the agents to analyze data and generate the report
ai_agent.run()
