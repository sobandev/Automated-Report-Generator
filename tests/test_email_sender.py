# tests/test_email_sender.py
import unittest
from unittest.mock import patch
from src.email_sender import send_email

class TestEmailSender(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        send_email('Test', 'test@example.com', 'report.pdf')
        self.assertTrue(mock_smtp.called)