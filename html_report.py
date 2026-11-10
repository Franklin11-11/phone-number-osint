import json
import os
import html
from collections import Counter
from datetime import datetime, timezone

REPORT_DIR = "evidence/reports"
OUTPUT_DIR = "evidence/exports"

os.makedirs(OUTPUT_DIR, exist_ok=True)

HTML_FILE = os.path.join(OUTPUT_DIR, "investigation_report.html")


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
            print(f"Could not read: {filename}")

    return reports


def generate_report():

    reports = load_reports()

    total = len(reports)
    valid = sum(r.get("valid_number") is True for r in reports)
    invalid = sum(r.get("valid_number") is False for r in reports)

    countries = Counter(
        str(r.get("country_code"))
        for r in reports
        if r.get("country_code") is not None
    )

    rows = ""

    for report in reports:

        status = (
            "VALID" if report.get("valid_number") is True
            else "INVALID" if report.get("valid_number") is False
            else "UNKNOWN"
        )

        rows += f"""
        <tr>
            <td>{html.escape(str(report.get('input_number', '')))}</td>
            <td>{html.escape(str(report.get('international_format', '')))}</td>
            <td>{html.escape(str(report.get('region') or 'Unknown'))}</td>
            <td>{html.escape(status)}</td>
            <td>{html.escape(str(report.get('original_carrier') or 'Unknown'))}</td>
            <td>{html.escape(', '.join(report.get('associated_timezones', [])))}</td>
            <td>{html.escape(str(report.get('timestamp_utc', '')))}</td>
        </tr>
        """

    country_rows = ""

    for code, count in countries.items():
        country_rows += f"<li>Country Code +{html.escape(code)}: {count}</li>"

    if not country_rows:
        country_rows = "<li>No country-code data available</li>"

    report_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Phone Number OSINT Investigation Report</title>

<style>
body {{
    font-family: Arial, sans-serif;
    background: #f4f6f9;
    margin: 30px;
    color: #222;
}}

header {{
    background: #172554;
    color: white;
    padding: 25px;
    border-radius: 8px;
}}

.cards {{
    display: flex;
    gap: 15px;
    margin: 25px 0;
    flex-wrap: wrap;
}}

.card {{
    background: white;
    padding: 20px;
    border-radius: 8px;
    flex: 1;
    min-width: 140px;
    box-shadow: 0 2px 6px #ddd;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    background: white;
    font-size: 13px;
}}

th, td {{
    padding: 12px;
    border: 1px solid #ddd;
    text-align: left;
}}

th {{
    background: #172554;
    color: white;
}}

tr:nth-child(even) {{
    background: #eef2ff;
}}

footer {{
    margin-top: 30px;
    font-size: 12px;
    color: #666;
}}
</style>
</head>

<body>

<header>
    <h1>Phone Number OSINT Investigation</h1>
    <p>Automated Numbering Metadata Analysis Report</p>
</header>

<section class="cards">

    <div class="card">
        <h3>Total Investigated</h3>
        <h2>{total}</h2>
    </div>

    <div class="card">
        <h3>Valid Numbers</h3>
        <h2>{valid}</h2>
    </div>

    <div class="card">
        <h3>Invalid Numbers</h3>
        <h2>{invalid}</h2>
    </div>

</section>

<h2>Country Code Distribution</h2>

<ul>
    {country_rows}
</ul>

<h2>Investigation Results</h2>

<table>
<thead>
<tr>
    <th>Input Number</th>
    <th>International Format</th>
    <th>Region</th>
    <th>Validity</th>
    <th>Carrier Metadata</th>
    <th>Timezone</th>
    <th>Timestamp (UTC)</th>
</tr>
</thead>

<tbody>
{rows}
</tbody>
</table>

<footer>
    <p>Generated: {datetime.now(timezone.utc).isoformat()}</p>
    <p>Privacy Notice: This report contains numbering metadata, not verified subscriber identity or live location.</p>
    <p>For authorized research and educational use only.</p>
</footer>

</body>
</html>
"""

    with open(HTML_FILE, "w") as file:
        file.write(report_html)

    print("\n========== HTML REPORT GENERATED ==========")
    print(f"Total investigations: {total}")
    print(f"Valid numbers: {valid}")
    print(f"Invalid numbers: {invalid}")
    print(f"Report location: {HTML_FILE}")


if __name__ == "__main__":
    generate_report()
