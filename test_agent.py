import os
from dotenv import load_dotenv

from app.agent.incident_agent import IncidentResponseAgent


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

agent = IncidentResponseAgent(api_key)


incident = """
Production API is returning 503 errors.
The problem started 10 minutes ago.
A database configuration change was made shortly before the errors started.
"""


result = agent.investigate(incident)

print("\n===== INCIDENT RESPONSE =====\n")
print(result)