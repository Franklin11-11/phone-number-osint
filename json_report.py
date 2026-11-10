import phonenumbers
import json
from datetime import datetime, timezone
from phonenumbers import geocoder, carrier, timezone as phone_timezone

def analyze_number(phone):
    try:
        number = phonenumbers.parse(phone, None)

        report = {
            "investigation_type": "Phone Number OSINT",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
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

        filename = "investigation_report.json"

        with open(filename, "w") as file:
            json.dump(report, file, indent=4)

        print("\n========== INVESTIGATION REPORT ==========")
        print(json.dumps(report, indent=4))
        print(f"\nReport saved successfully: {filename}")

    except phonenumbers.NumberParseException as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    phone = input("Enter phone number (+country code): ").strip()
    analyze_number(phone)
