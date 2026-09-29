
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6IClQFW-BJIEnzSQg60OhwTzy62Rca--7yBx2Qa2y50JQ")

for model in client.models.list():
    print(model.name)