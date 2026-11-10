import json
import os
from collections import Counter

REPORT_DIR = "evidence/reports"


def load_reports():
    reports = []

    for filename in os.listdir(REPORT_DIR):

        if not filename.endswith(".json"):
            continue

        filepath = os.path.join(REPORT_DIR, filename)

        try:
            with open(filepath, "r") as file:
                data = json.load(file)

            if data.get("investigation_type") == "Batch Phone Number OSINT":
                reports.append(data)

        except (json.JSONDecodeError, OSError):
            print(f"Warning: Could not read {filename}")

    return reports


def display_dashboard():

    reports = load_reports()

    total = len(reports)

    valid = sum(1 for r in reports if r.get("valid_number") is True)

    invalid = sum(1 for r in reports if r.get("valid_number") is False)

    country_codes = Counter(
        str(r.get("country_code"))
        for r in reports
        if r.get("country_code") is not None
    )

    print("\n" + "=" * 55)
    print("          PHONE NUMBER OSINT DASHBOARD")
    print("=" * 55)

    print(f"\nTotal Numbers Investigated: {total}")
    print(f"Valid Numbers:             {valid}")
    print(f"Invalid Numbers:           {invalid}")

    print("\n" + "-" * 55)
    print("COUNTRY CODE DISTRIBUTION")
    print("-" * 55)

    for code, count in country_codes.items():
        print(f"Country Code +{code}: {count}")

    print("\n" + "-" * 55)
    print("INDIVIDUAL INVESTIGATION RESULTS")
    print("-" * 55)

    for report in reports:

        status = (
            "VALID" if report.get("valid_number") is True
            else "INVALID" if report.get("valid_number") is False
            else "UNKNOWN"
        )

        print(f"Number: {report.get('input_number')}")
        print(f"Status: {status}")
        print(f"Region: {report.get('region')}")
        print("-" * 55)

    print("\nDASHBOARD GENERATION COMPLETE")


if __name__ == "__main__":
    display_dashboard()
