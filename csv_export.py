import csv
import json
import os

REPORT_DIR = "evidence/reports"
EXPORT_DIR = "evidence/exports"

os.makedirs(EXPORT_DIR, exist_ok=True)

CSV_FILE = os.path.join(EXPORT_DIR, "investigation_summary.csv")

FIELDS = [
    "input_number",
    "international_format",
    "e164_format",
    "country_code",
    "region",
    "valid_number",
    "possible_number",
    "geographical_description",
    "original_carrier",
    "associated_timezones",
    "timestamp_utc"
]


def export_reports():

    reports = []

    for filename in os.listdir(REPORT_DIR):

        if not filename.endswith(".json"):
            continue

        filepath = os.path.join(REPORT_DIR, filename)

        try:
            with open(filepath, "r") as file:
                data = json.load(file)

            if data.get("investigation_type") == "Batch Phone Number OSINT":
                data["associated_timezones"] = ", ".join(
                    data.get("associated_timezones", [])
                )
                reports.append(data)

        except (json.JSONDecodeError, OSError):
            print(f"Could not process: {filename}")

    with open(CSV_FILE, "w", newline="") as file:

        writer = csv.DictWriter(file, fieldnames=FIELDS, extrasaction="ignore")

        writer.writeheader()
        writer.writerows(reports)

    print("\n========== CSV EXPORT COMPLETE ==========")
    print(f"Total records exported: {len(reports)}")
    print(f"Export location: {CSV_FILE}")


if __name__ == "__main__":
    export_reports()
