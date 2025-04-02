# src/main.py
from . import config
from .database import fetch_data
from .report_generator import generate_report
from .email_sender import send_email

def main():
    # Fetch data from Supabase
    data = fetch_data('sales_data')
    if not data:
        print("No data fetched from the database.")
        return
    
    # Generate the report
    report_path = 'report.pdf'
    generate_report(data, report_path)
    print(f"Report generated: {report_path}")

    # Send the email
    send_email('Daily Sales Report', 'recipient@example.com', report_path)
    print("Email sent successfully.")

if __name__ == '__main__':
    main()