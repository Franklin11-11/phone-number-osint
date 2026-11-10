import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def analyze_phone_number():

    print("=" * 55)
    print("          PHONE NUMBER OSINT ANALYZER")
    print("=" * 55)

    number = input("\nEnter test phone number (+country code): ")

    try:
        parsed = phonenumbers.parse(number, None)

        print("\n========== INVESTIGATION RESULTS ==========")

        print(
            "International Format:",
            phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
        )

        print("Country Code:", parsed.country_code)

        print(
            "Region:",
            phonenumbers.region_code_for_number(parsed)
        )

        print(
            "Valid Number:",
            phonenumbers.is_valid_number(parsed)
        )

        print(
            "Possible Number:",
            phonenumbers.is_possible_number(parsed)
        )

        print(
            "Geographical Description:",
            geocoder.description_for_number(parsed, "en")
        )

        print(
            "Original Carrier:",
            carrier.name_for_number(parsed, "en")
        )

        print(
            "Associated Timezones:",
            timezone.time_zones_for_number(parsed)
        )

        print("\n========== ANALYSIS COMPLETE ==========")

        print("\nNote: These results represent numbering metadata.")
        print("They do not establish subscriber identity or live GPS location.")

    except phonenumbers.NumberParseException as error:

        print("\n[ERROR]", error)


if __name__ == "__main__":
    analyze_phone_number()
