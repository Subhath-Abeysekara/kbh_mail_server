import random
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle ,  Paragraph, Spacer
from reportlab.lib import colors
from datetime import datetime, timedelta

from sendMail import send_mail_product, send_ml_sales

page_width, page_height = letter
num_rows = 10


def kbh_product_report(data):
    code = data['code']
    name = data['name']
    period = data['period']
    total_sales = data['total_sales']
    total_income = data['total_income']
    total_balance = data['total_balance']
    info = data['daily_info']
    pdf_file = "table_kbh_product_report.pdf"
    header_row = ['Date', 'Initial Stock', 'Addons', 'Sales', 'Balance', 'Cash Income', 'Card Income']
    data = [header_row]
    for row in info:
        data.append(row)
    print(data)
    num_rows = len(data)
    col_widths = [600 / len(header_row)] * len(header_row)
    row_heights = [30] * num_rows
    table = Table(data, colWidths=col_widths, rowHeights=row_heights)
    header_color = colors.lightblue
    row_color_1 = colors.whitesmoke
    row_color_2 = colors.lightgrey
    style = TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for headers
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Increase font size for better readability
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # White text for headers
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),  # Extra padding for headers
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Gridlines
        ('BACKGROUND', (0, 0), (-1, 0), header_color),  # Header background color
    ])
    for row_idx in range(1, len(data)):
        bg_color = row_color_1 if row_idx % 2 == 0 else row_color_2
        style.add('BACKGROUND', (0, row_idx), (-1, row_idx), bg_color)
    doc = SimpleDocTemplate(pdf_file, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    table.setStyle(style)
    styles = getSampleStyleSheet()
    header = Paragraph("Product Report", styles["Title"])
    sub_header = Paragraph(
        f"Product Name : {name}",
        styles["Normal"])
    sub_header2 = Paragraph(
        f"Product Code : {code}",
        styles["Normal"])
    sub_header3 = Paragraph(
        f"Period : {period}",
        styles["Normal"])
    sub_header4 = Paragraph(
        f"Total Sales : {str(total_sales)}",
        styles["Normal"])
    sub_header5 = Paragraph(
        f"Total Income : {str(total_income)}",
        styles["Normal"])
    sub_header6 = Paragraph(
        f"Total Balance : {str(total_balance)}",
        styles["Normal"])
    doc.build([header, Spacer(1, 12), sub_header, Spacer(1, 12), sub_header2, Spacer(1, 12),sub_header3, Spacer(1, 12), sub_header4, Spacer(1, 12),sub_header5, Spacer(1, 12), sub_header6, Spacer(1, 12), table])
    print(f"✅ PDF created with improved row height: {pdf_file}")
    send_mail_product()


def kbh_sales_report(info):
    pdf_file = "table_kbh_sales_report.pdf"
    header_row = ['Product Name', 'Product Code', 'Initial Stock', 'Addons', 'Sales', 'Balance', 'Cash Income',
                  'Card Income']
    today_date = datetime.today().strftime("%d/%m/%Y")
    data = [header_row]
    for row in info:
        data.append(row)
    num_rows = len(data)
    col_widths = [600 / len(header_row)] * len(header_row)  # Adjust column widths
    row_heights = [30] * num_rows  # Set taller header row, standard row height
    table = Table(data, colWidths=col_widths, rowHeights=row_heights)
    header_color = colors.lightblue  # Light blue for headers
    row_color_1 = colors.whitesmoke  # Light grey for alternate rows
    row_color_2 = colors.lightgrey  # Slightly darker grey for contrast
    style = TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for headers
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Increase font size for better readability
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Black text for headers
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),  # Extra padding for headers
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Gridlines
        ('BACKGROUND', (0, 0), (-1, 0), header_color),  # Header background color
    ])
    for row_idx in range(1, len(data)):
        bg_color = row_color_1 if row_idx % 2 == 0 else row_color_2
        style.add('BACKGROUND', (0, row_idx), (-1, row_idx), bg_color)
    table.setStyle(style)
    doc = SimpleDocTemplate(pdf_file, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    styles = getSampleStyleSheet()
    header = Paragraph(f"Sales Report - {today_date}", styles["Title"])
    doc.build([
        header, Spacer(1, 12), table
    ])
    print(f"✅ PDF created with bakery sales data: {pdf_file}")
    send_ml_sales()

def kbh_order_report(data):
    data = data['data']
    date = data['date']
    pdf_file = "table_kbh_order_report.pdf"
    headers = ["Order Code","Product Name", "Product Code", "Placed Date", "Pickup Date", "Delivery Status", "Amount", "Price",
               "Advance", "Contact", "Address"]
    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    formatted_data = [[Paragraph(cell, normal_style) for cell in headers]]
    for row in data:
        formatted_data.append([Paragraph(str(cell), normal_style) for cell in row])
    col_widths = [550 / len(headers)] * len(headers)
    table = Table(formatted_data, colWidths=col_widths)
    style = TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for headers
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Font size for all text
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Black text for headers
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical align to middle
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),  # Extra padding for headers
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Gridlines
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),  # Header background color
    ])
    for row_idx in range(1, len(formatted_data)):
        bg_color = colors.whitesmoke if row_idx % 2 == 0 else colors.lightgrey
        style.add('BACKGROUND', (0, row_idx), (-1, row_idx), bg_color)
    table.setStyle(style)
    doc = SimpleDocTemplate(pdf_file, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    title = Paragraph("Order Report", styles["Title"])
    sub_header = Paragraph(
        f"Date : {date}",
        styles["Normal"])
    doc.build([title, Spacer(1, 12), sub_header, Spacer(1, 12), table])
    print(f"✅ PDF saved successfully: {pdf_file}")

# # Run the function with example values
# kbh_sales_report()
# kbh_order_report()
# kbh_today_placed_order_report()
# kbh_today_pickup_order_report()
# kbh_product_report(name="Fish Bun" , code="001" , period="23/03/2025 - 27/03/2025" , total_sales=500 , total_income=25000 , total_balance=50)
#
# data = {'name': 'Cinnamon Roll', 'code': '010', 'period': '2025-04-01 - 2025-04-05', 'total_sales': 27, 'total_balance': 15, 'total_income': 800, 'daily_info': [['2025-04-01', 10, 10, 0, 20, 200, 0], ['2025-04-02', 10, 12, 15, 7, 600, 0]]}
# kbh_product_report(data)