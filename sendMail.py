import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_email = 'icodeinnovahostingservice@gmail.com'
sender_password = 'hnykgvqgyvorghrb'
receiver = 'newkanduratabakehouse@gmail.com'

def send_mail_pdf(body , subject , pdfname):
    # put your email here
    # receiver = 'subath.abeysekara@gmail.com'

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))


    # open the file in bynary
    binary_pdf = open(pdfname, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    # payload = MIMEBase('application', 'pdf', Name=pdfname)
    payload.set_payload((binary_pdf).read())

    # enconding the binary into base64
    encoders.encode_base64(payload)

    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)

    # use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)

    # enable security
    session.starttls()

    # login with mail_id and password
    session.login(sender_email, sender_password)

    text = message.as_string()
    session.sendmail(sender_email, receiver, text)
    session.quit()
    return {
        "state": True,
        "message": 'mail sent'
    }

def send_mail_all_orders():
    body = '''Get Your Report Here
        '''
    pdfname = 'table_kbh_order_report.pdf'
    subject = 'Order Report'
    return send_mail_pdf(body, subject, pdfname)

def send_mail_product():
    body = '''Get Your Document Here
    '''
    subject = 'Product Report'
    pdfname = "table_kbh_product_report.pdf"
    return send_mail_pdf(body, subject, pdfname)

def send_ml_sales():
    body = '''Get Your Document Here
    '''
    subject = 'Product Sales Report'
    pdfname = "table_kbh_sales_report.pdf"
    return send_mail_pdf(body, subject, pdfname)

def send_ml_hourly_sales():
    body = '''Get Your Document Here
    '''
    subject = 'Hourly Sales Report'
    pdfname = "table_kbh_hourly_sales_report.pdf"
    return send_mail_pdf(body, subject, pdfname)