import phonenumbers
import json
import os
from datetime import datetime, timezone
from phonenumbers import geocoder, carrier, timezone as phone_timezone

OUTPUT_DIR = "evidence/reports"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def analyze_number(phone):

    try:
        number = phonenumbers.parse(phone, None)

        timestamp = datetime.now(timezone.utc).isoformat()

        report = {
            "investigation_type": "Batch Phone Number OSINT",
            "timestamp_utc": timestamp,
            "input_number": phone,
            "international_format": phonenumbers.format_number(
                number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            ),
            "e164_format": phonenumbers.format_number(
                number, phonenumbers.PhoneNumberFormat.E164
            ),
            "country_code": number.country_code,
            "region": geocoder.region_code_for_number(number),
            "valid_number": phonenumbers.is_valid_number(number),
            "possible_number": phonenumbers.is_possible_number(number),
            "geographical_description": geocoder.description_for_number(
                number, "en"
            ),
            "original_carrier": carrier.name_for_number(number, "en"),
            "associated_timezones": list(
                phone_timezone.time_zones_for_number(number)
            )
        }

        safe_name = phone.replace("+", "").replace(" ", "")
        filename = f"{OUTPUT_DIR}/{safe_name}.json"

        with open(filename, "w") as file:
            json.dump(report, file, indent=4)

        print(f"\nAnalysis completed: {phone}")
        print(f"Valid: {report['valid_number']}")
        print(f"Report: {filename}")

    except phonenumbers.NumberParseException as error:
        print(f"\nUnable to parse {phone}: {error}")


if __name__ == "__main__":

    print("=" * 50)
    print("BATCH PHONE NUMBER OSINT ANALYZER")
    print("=" * 50)

    numbers = input(
        "\nEnter phone numbers separated by commas: "
    ).split(",")

    for phone in numbers:
        phone = phone.strip()

        if phone:
            analyze_number(phone)

    print("\n========== BATCH ANALYSIS COMPLETE ==========")
