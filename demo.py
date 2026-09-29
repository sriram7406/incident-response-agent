from memory.hindsight import HindsightMemory
from analyzer.service import IncidentAnalysisService


def print_section(title):

    print("\n")
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():

    print_section(
        "INCIDENT RESPONSE AGENT - MEMBER 2"
    )

    # Initialize memory
    memory = HindsightMemory()

    # Initialize analysis service
    service = IncidentAnalysisService(
        memory
    )

    # Simulated production incident
    incident = """
    Payment API started returning HTTP 500 errors
    after the latest deployment.

    Database connections are timing out and
    payment requests are failing.
    """

    print_section(
        "1. RAW INCIDENT"
    )

    print(incident)

    # Analyze incident
    report = service.analyze_incident(
        incident,
        top_k=5
    )

    # -------------------------
    # Incident analysis
    # -------------------------

    print_section(
        "2. INCIDENT ANALYSIS"
    )

    analysis = report["incident"]

    print(
        "Service:",
        analysis["service"]
    )

    print(
        "Incident Type:",
        analysis["incident_type"]
    )

    print(
        "Severity:",
        analysis["severity"]
    )

    print(
        "Symptoms:",
        analysis["symptoms"]
    )

    print(
        "Trigger:",
        analysis["trigger"]
    )

    print(
        "Root Cause Hypothesis:",
        analysis[
            "root_cause_hypothesis"
        ]
    )

    # -------------------------
    # Historical evidence
    # -------------------------

    print_section(
        "3. HISTORICAL EVIDENCE"
    )

    evidence = report[
        "historical_evidence"
    ]

    print(
        "\nSimilar Incidents:"
    )

    for incident in evidence[
        "similar_incidents"
    ]:

        print(
            "-",
            incident["incident_id"],
            "|",
            incident["title"],
            "| similarity:",
            incident["similarity"]
        )

    print(
        "\nCommon Root Causes:"
    )

    for cause in evidence[
        "common_root_causes"
    ]:

        print(
            "-",
            cause["value"],
            "| count:",
            cause["count"]
        )

    print(
        "\nSuccessful Solutions:"
    )

    for solution in evidence[
        "successful_solutions"
    ]:

        print(
            "-",
            solution["value"],
            "| count:",
            solution["count"]
        )

    print(
        "\nFailed Attempts:"
    )

    for failure in evidence[
        "failed_attempts"
    ]:

        print(
            "-",
            failure["value"]
        )

    print(
        "\nRecurring Patterns:"
    )

    for pattern in evidence[
        "recurring_patterns"
    ]:

        print(
            "-",
            pattern["pattern"],
            "| count:",
            pattern["count"]
        )

    # -------------------------
    # AI reasoning
    # -------------------------

    print_section(
        "4. HINDSIGHT REASONING"
    )

    reasoning = report.get(
        "ai_reasoning",
        {}
    )

    print(
        "Assessment:",
        reasoning.get(
            "assessment",
            "N/A"
        )
    )

    print(
        "\nRecommended Actions:"
    )

    for action in reasoning.get(
        "recommended_actions",
        []
    ):

        print(
            "-",
            action
        )

    print(
        "\nWarnings:"
    )

    for warning in reasoning.get(
        "warnings",
        []
    ):

        print(
            "-",
            warning
        )

    # -------------------------
    # Final recommendation
    # -------------------------

    print_section(
        "5. FINAL RECOMMENDATION"
    )

    print(
        report["recommendation"]
    )

    print(
        "\nConfidence:",
        report["confidence"]
    )

    print_section(
        "MEMBER 2 COMPLETE"
    )


if __name__ == "__main__":

    main()