# src/report_generator.py
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO)

def generate_report(data: list, output_file: str):
    """Generate a PDF report with a title, table, and chart."""
    if not data:
        logging.info("No data available to generate the report.")
        return

    doc = SimpleDocTemplate(output_file, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    title = Paragraph("Electronics Sales Report", styles['Title'])
    elements.append(title)

    if data:
        table_data = [list(data[0].keys())] + [list(row.values()) for row in data]
        table = Table(table_data)
        elements.append(table)

    if data:
        plt.figure(figsize=(8, 4))
        plt.bar([row['product'] for row in data], [row['sales'] for row in data])
        plt.xlabel('Product')
        plt.ylabel('Sales')
        plt.title('Sales Overview')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        chart_path = 'sales_chart.png'
        plt.savefig(chart_path)
        plt.close()
        elements.append(Image(chart_path, width=400, height=300))

    doc.build(elements)