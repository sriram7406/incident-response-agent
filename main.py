import json

from models.incident import Incident


def load_incidents():

    with open("data/incidents.json", "r") as file:
        data = json.load(file)

    incidents = []

    for item in data:
        incident = Incident(
            incident_id=item["incident_id"],
            title=item["title"],
            service=item["service"],
            severity=item["severity"],
            symptoms=item["symptoms"],
            logs=item["logs"],
            root_cause=item["root_cause"],
            solution=item["solution"],
            resolution_steps=item["resolution_steps"],
            runbook=item["runbook"],
            outcome=item["outcome"],
            timestamp=item["timestamp"]
        )

        incidents.append(incident)

    return incidents


def main():

    incidents = load_incidents()

    print("===================================")
    print(" INCIDENT MEMORY SYSTEM")
    print("===================================")

    print("Total incidents:", len(incidents))

    print()

    for incident in incidents:

        print("Incident ID :", incident.incident_id)
        print("Title       :", incident.title)
        print("Service     :", incident.service)
        print("Severity    :", incident.severity)
        print("Root Cause  :", incident.root_cause)
        print("Solution    :", incident.solution)
        print("Outcome     :", incident.outcome)

        print("-----------------------------------")


if __name__ == "__main__":
    main()