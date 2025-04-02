# tests/test_report_generator.py
import unittest
from src.report_generator import generate_report

class TestReportGenerator(unittest.TestCase):
    def test_generate_report_empty_data(self):
        with self.assertLogs(level='INFO') as log:
            generate_report([], 'empty_report.pdf')
        self.assertIn("No data available to generate the report.", log.output[0])