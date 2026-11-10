import unittest
import json
import os
import tempfile
from pathlib import Path
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

import json_report
import batch_analyzer


class JSONReportTests(unittest.TestCase):

    def test_valid_number_generates_report(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            original_dir = os.getcwd()

            try:
                os.chdir(temp_dir)

                with redirect_stdout(StringIO()):
                    json_report.analyze_number("+2348034567892")

                report_path = Path("investigation_report.json")

                self.assertTrue(report_path.exists())

                with report_path.open() as file:
                    report = json.load(file)

                self.assertTrue(report["valid_number"])
                self.assertEqual(report["country_code"], 234)
                self.assertEqual(report["e164_format"], "+2348034567892")

            finally:
                os.chdir(original_dir)

    def test_invalid_but_parseable_number(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            original_dir = os.getcwd()

            try:
                os.chdir(temp_dir)

                with redirect_stdout(StringIO()):
                    json_report.analyze_number("+12005550123")

                with open("investigation_report.json") as file:
                    report = json.load(file)

                self.assertFalse(report["valid_number"])
                self.assertTrue(report["possible_number"])

            finally:
                os.chdir(original_dir)

    def test_unparseable_number(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            original_dir = os.getcwd()

            try:
                os.chdir(temp_dir)
                output = StringIO()

                with redirect_stdout(output):
                    json_report.analyze_number("not-a-number")

                self.assertIn("Invalid input", output.getvalue())
                self.assertFalse(
                    Path("investigation_report.json").exists()
                )

            finally:
                os.chdir(original_dir)


class BatchAnalyzerTests(unittest.TestCase):

    def test_batch_analysis_generates_report(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir) / "reports"
            output_dir.mkdir()

            with patch.object(
                batch_analyzer, "OUTPUT_DIR", str(output_dir)
            ):
                with redirect_stdout(StringIO()):
                    batch_analyzer.analyze_number("+2348034567892")

            report_path = output_dir / "2348034567892.json"

            self.assertTrue(report_path.exists())

            with report_path.open() as file:
                report = json.load(file)

            self.assertTrue(report["valid_number"])
            self.assertEqual(report["country_code"], 234)

    def test_batch_analyzer_handles_invalid_input(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir) / "reports"
            output_dir.mkdir()

            output = StringIO()

            with patch.object(
                batch_analyzer, "OUTPUT_DIR", str(output_dir)
            ):
                with redirect_stdout(output):
                    batch_analyzer.analyze_number("not-a-number")

            self.assertIn("Unable to parse", output.getvalue())
            self.assertEqual(list(output_dir.iterdir()), [])


if __name__ == "__main__":
    unittest.main()

