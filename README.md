# Phone Number OSINT Investigation

An educational Python-based OSINT tool for analysing phone-number numbering metadata, validating number formats, and generating structured investigation reports.

## Project Overview

This project demonstrates how publicly available phone-number metadata can be analysed using Python and the `phonenumbers` library.

It supports individual and batch analysis, JSON report generation, investigation summaries, CSV exports, and HTML reports.

The project is designed for cybersecurity education, OSINT practice, and authorized research.

## Features

- Phone-number parsing and validation.
- International and national number formatting.
- Country and geographical numbering metadata.
- Original carrier metadata lookup.
- Associated timezone identification.
- Individual JSON investigation reports.
- Batch phone-number analysis.
- Investigation summary dashboard.
- CSV report export.
- HTML investigation report generation.
- Error handling for unparseable numbers.

## Technologies Used

- Python 3
- phonenumbers
- JSON
- CSV
- HTML
- Linux / Kali Linux

## Project Structure

```text
phone-number-osint/
│
├── phone_analyzer.py
├── json_report.py
├── batch_analyzer.py
├── dashboard.py
├── csv_export.py
├── html_report.py
│
├── investigation_report.json
│
├── evidence/
│   ├── reports/
│   └── exports/
│
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd phone-number-osint
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install the dependency:

```bash
pip install phonenumbers
```

## Usage

### 1. Basic Phone Number Analysis

```bash
python3 phone_analyzer.py
```

### 2. Generate an Individual JSON Report

```bash
python3 json_report.py
```

### 3. Perform Batch Analysis

```bash
python3 batch_analyzer.py
```

Enter phone numbers separated by commas, including their international country codes.

Example:

```text
+2348034567892, +12005550123
```

### 4. View the Investigation Dashboard

```bash
python3 dashboard.py
```

### 5. Export Investigation Results to CSV

```bash
python3 csv_export.py
```

### 6. Generate an HTML Investigation Report

```bash
python3 html_report.py
```

The generated HTML report is saved in:

```text
evidence/exports/investigation_report.html
```

## Sample Investigation Results

The project was tested using two sample phone-number inputs.

| Input Number | Region | Validation | Carrier Metadata | Timezone |
|---|---|---|---|---|
| +2348034567892 | Nigeria | Valid | MTN | Africa/Lagos |
| +12005550123 | Unknown | Invalid | Unknown | Etc/Unknown |

The test demonstrated:

- Successful Nigerian number validation.
- Detection of an invalid number.
- Country-code identification.
- Metadata extraction.
- Batch report generation.
- CSV and HTML report generation.

## Evidence and Reporting

Investigation outputs are organised into:

- `evidence/reports/` — Individual JSON reports.
- `evidence/exports/` — CSV and HTML exports.

Screenshots documenting the development and testing process are maintained separately.

## Important Limitations

This tool analyses phone-number numbering metadata. It does not:

- Identify or verify a subscriber's identity.
- Retrieve private subscriber records.
- Track a phone's live GPS location.
- Confirm a number's current mobile network operator.
- Access private telecommunications databases.

Carrier information is based on numbering-library metadata and may not reflect current network assignment because of mobile number portability.

## Ethical Considerations

This project is intended for educational purposes, authorized OSINT research, and cybersecurity learning.

Always respect privacy, applicable laws, and data-protection requirements when handling phone numbers.

## Author

**Franklin Chukwuemeka**

Cybersecurity | SOC Analysis | OSINT | Security Research

GitHub: https://github.com/Franklin11-11

## Project Screenshots

### Individual JSON Investigation
![JSON Investigation](evidence/screenshots/09-automated-json-investigation-report.png)

### JSON Report Validation
![JSON Validation](evidence/screenshots/10-json-report-validation-and-export.png)

### Batch Analysis
![Batch Analysis](evidence/screenshots/11-batch-phone-number-analysis.png)

### Investigation Dashboard
![Investigation Dashboard](evidence/screenshots/12-investigation-summary-dashboard.png)

### CSV Export
![CSV Export](evidence/screenshots/13-csv-investigation-export.png)

### HTML Investigation Report
![HTML Report](evidence/screenshots/14-html-investigation-report.png)
