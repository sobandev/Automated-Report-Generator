# Automated Report Generation Tool

![Project Status](https://img.shields.io/badge/status-completed-brightgreen)  
![Python](https://img.shields.io/badge/python-3.10+-blue)  
![License](https://img.shields.io/badge/license-MIT-green)

## Overview

The **Automated Report Generation Tool** is a Python-based application that automates the process of generating and distributing sales reports. It fetches sales data from a Supabase database, creates a professional PDF report with tables and charts, and emails the report to specified recipients using Gmail with 2FA support. This tool is ideal for businesses looking to streamline their reporting workflows, saving time and reducing manual effort.

This project demonstrates my expertise in Python development, API integration, data visualization, and secure email automation—skills I bring to every client project on Upwork.

## Features

- **Data Fetching**: Retrieves sales data from a Supabase database using the Supabase Python client.
- **Report Generation**: Creates a PDF report with:
  - A title ("Electronics Sales Report").
  - A table of sales data (e.g., product names and sales figures).
  - A bar chart visualizing sales performance using Matplotlib.
- **Email Automation**: Sends the generated report as an email attachment via Gmail, supporting 2FA with app-specific passwords.
- **Error Handling**: Includes robust error handling for database connections, report generation, and email sending.
- **Configurability**: Supports configuration via a JSON file (`config.json`) for table names and email recipients, with optional command-line overrides.
- **Testing**: Comes with a comprehensive test suite using `unittest` to ensure reliability, covering edge cases like empty datasets and email failures.
- **Mock Data**: Includes realistic mock data for an electronics store (e.g., MacBook Pro, iPhone 15 Pro) to demonstrate functionality out of the box.

## Sample Output

The tool generates a PDF report (`report.pdf`) with the following content, based on the mock data:

**Electronics Sales Report**

| id | product                | sales |
|----|------------------------|-------|
| 1  | MacBook Pro 14"        | 150   |
| 2  | iPhone 15 Pro          | 200   |
| 3  | Samsung Galaxy S23     | 180   |
| 4  | AirPods Pro            | 120   |
| 5  | USB-C Charger 65W      | 90    |
| 6  | Dell XPS 13            | 140   |
| 7  | Sony WH-1000XM5 Headphones | 110   |

**Sales Overview**  
(A bar chart visualizing the sales data, with products on the x-axis and sales figures on the y-axis.)

## Project Structure

```
automated_report_generator/
├── src/
│   ├── __init__.py
│   ├── main.py                # Entry point to run the application
│   ├── config.py              # Configuration for Supabase and email (excluded from Git)
│   ├── config_template.py     # Template for config.py
│   ├── database.py            # Supabase connection and data fetching
│   ├── report_generator.py    # PDF report generation logic
│   ├── email_sender.py        # Email sending functionality
│   └── config.json            # Configuration file for table name and email recipient
├── tests/
│   ├── test_database.py       # Tests for database functions
│   ├── test_report_generator.py # Tests for report generation
│   └── test_email_sender.py   # Tests for email sending
├── docs/
│   ├── mock_data.sql          # SQL script to populate Supabase with mock data
│   ├── requirements.txt       # List of Python dependencies
│   └── README.md              # This file
└── venv/                      # Virtual environment (excluded from Git)
```

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- A Supabase account with a project set up
- A Gmail account with 2FA enabled and an app-specific password generated

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sobandev/automated-report-generator.git
   cd automated-report-generator
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r docs/requirements.txt
   ```
   Dependencies include `supabase`, `reportlab`, and `matplotlib`.

4. **Configure Supabase and Gmail**:
   - Copy `src/config_template.py` to `src/config.py`:
     ```bash
     copy src\config_template.py src\config.py  # On Windows
     # cp src/config_template.py src/config.py  # On macOS/Linux
     ```
   - Create a Supabase project and note your project URL and API key.
   - Run the SQL script in `docs/mock_data.sql` via the Supabase SQL Editor to create and populate the `sales_data` table with mock data:
     ```sql
     CREATE TABLE sales_data (
         id SERIAL PRIMARY KEY,
         product VARCHAR(255) NOT NULL,
         sales INTEGER NOT NULL
     );

     INSERT INTO sales_data (product, sales) VALUES
         ('MacBook Pro 14"', 150),
         ('iPhone 15 Pro', 200),
         ('Samsung Galaxy S23', 180),
         ('AirPods Pro', 120),
         ('USB-C Charger 65W', 90),
         ('Dell XPS 13', 140),
         ('Sony WH-1000XM5 Headphones', 110);
     ```
   - Enable 2FA on your Gmail account and generate an app-specific password (under "App passwords" in your Google Account settings).
   - Update `src/config.py` with your Supabase and Gmail credentials:
     ```python
     # src/config.py
     SUPABASE_URL = 'your_supabase_url'
     SUPABASE_KEY = 'your_supabase_key'
     EMAIL_USER = 'your_email@gmail.com'
     EMAIL_PASSWORD = 'your_app_specific_password'
     ```

5. **Configure Email Recipient**:
   - Update `src/config.json` with the desired table name and email recipient:
     ```json
     {
         "table_name": "sales_data",
         "email_recipient": "recipient@example.com"
     }
     ```

## Usage

Run the application from the root directory:

```bash
python -m src.main
```

### Optional Command-Line Arguments
Override the default table name or email recipient:

```bash
python -m src.main --table "orders" --recipient "newrecipient@example.com"
```

### Expected Output
The script will:
1. Fetch sales data from Supabase.
2. Generate a PDF report (`report.pdf`) with a table and chart.
3. Send the report as an email attachment to the specified recipient.

Example output in the terminal:
```
INFO:httpx:HTTP Request: GET https://your-supabase-url/rest/v1/sales_data?select=%2A "HTTP/2 200 OK"
Report generated: report.pdf
Email sent successfully.
```

## Running Tests

The project includes a test suite to ensure reliability. Run the tests from the root directory:

```bash
python -m unittest discover -s tests
```

The tests cover:
- Database connectivity and data fetching.
- Report generation with empty datasets.
- Email sending functionality (mocked to avoid real email sends).

## Technologies Used

- **Python 3.10+**: Core programming language.
- **Supabase**: Cloud-based PostgreSQL database for data storage.
- **ReportLab**: For generating PDF reports with tables.
- **Matplotlib**: For creating bar charts in the report.
- **smtplib**: For sending emails via Gmail with 2FA support.
- **unittest**: For automated testing.

## Why This Project Stands Out

This tool isn’t just another automation script—it’s a complete, **ready-to-use solution** for businesses that need **fast, reliable, and secure** sales reporting. Here’s why it’s special:

- **Saves Time & Effort** – Automates data fetching, report generation, and email delivery, eliminating manual work.  
- **Seamless Cloud Integration** – Uses **Supabase** (a powerful PostgreSQL-based backend) to ensure smooth, real-time data retrieval.  
- **Professional Reports** – Generates **visually appealing, data-driven PDF reports** with tables and charts for easy analysis.  
- **Secure Email Automation** – Sends reports via **Gmail with 2FA support**, keeping security a top priority.  
- **Easy to Customize** – Configure everything from table names to email recipients using a simple **JSON file or CLI options**.  
- **Rock-Solid Reliability** – Built with **robust error handling** and **unit-tested** to handle failures gracefully.  

This project highlights my expertise in **Python automation, API integration, data visualization, and secure email workflows**—essential skills for businesses looking to streamline operations and make data-driven decisions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For inquiries or freelance opportunities, feel free to reach out to me on [Upwork](https://www.upwork.com/freelancers/~014a5fe0f5463ea4a3) or via email at [sobanusman2020@gmail.com](mailto:sobanusman2020@gmail.com).

