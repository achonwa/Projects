import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import sqlite3
import mysql.connector
from oauth2client.service_account import ServiceAccountCredentials
import gspread

#  SMTP setup
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_html_email(
    smtp_email, 
    smtp_password, 
    recipient_email, 
    subject, 
    html_content, 
    custom_sender_name, 
    custom_sender_email, 
    reply_to=None
):
    email_message = MIMEMultipart()
    email_message['From'] = formataddr((custom_sender_name, custom_sender_email))
    email_message['To'] = recipient_email
    email_message['Subject'] = subject
    if reply_to:
        email_message['Reply-To'] = reply_to
    
    email_message.attach(MIMEText(html_content, 'html'))
    
    server = None
    try:
        smtplib.SMTP(SMTP_SERVER, SMTP_PORT)  #CONNECT TO SMTP SERVER
        server.starttls()
        server.login(smtp_email, smtp_password)
        server.sendmail(smtp_email, recipient_email, email_message.as_string())
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f'Failed to send email to {recipient_email}. Error: {e}')
    finally:
        server.quit()

def read_emails_from_local_file(file_path):
    # Assumes a CSV file with a column named "email"
    df = pd.read_csv(file_path)
    return df['email'].tolist()

def read_emails_from_google_sheets(sheet_url, credentials_json_path):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_json_path, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(sheet_url).sheet1
    emails = sheet.col_values(1)  # Assuming emails are in the first column
    return emails[1:]  # Skipping header if there's one

def read_emails_from_database(db_type, db_name, query, user=None, password=None, host="localhost"):
    if db_type == "sqlite":
        conn = sqlite3.connect(db_name)
    elif db_type == "mysql":
        conn = mysql.connector.connect(
            user=user, password=password, host=host, database=db_name
        )
    else:
        raise ValueError("Unsupported database type. Use 'sqlite' or 'mysql'.")
    
    cursor = conn.cursor()
    cursor.execute(query)
    emails = [row[0] for row in cursor.fetchall()]
    conn.close()
    return emails

# Usage example
smtp_email = "your_email@gmail.com"
smtp_password = "your_app_password"
subject = "Welcome to Our Service!"
html_file_path = "email_template.html"  # Path to the HTML file

# Read HTML content
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Sender details
custom_sender_name = "Your Company Name"
custom_sender_email = "no-reply@yourcompany.com"
reply_to_email = "support@yourcompany.com"

# Get email lists from different sources
# Example: Read emails from a local CSV file
local_emails = read_emails_from_local_file("emails.csv")

# Example: Read emails from Google Sheets
google_sheets_emails = read_emails_from_google_sheets("GOOGLE_SHEETS_URL", "credentials.json")

# Example: Read emails from a SQLite or MySQL database
# SQLite example
sqlite_emails = read_emails_from_database("sqlite", "emails.db", "SELECT email FROM users")

# MySQL example
# mysql_emails = read_emails_from_database("mysql", "database_name", "SELECT email FROM users", user="username", password="password")

# Combine all email lists into one (optional)
all_emails = set(local_emails + google_sheets_emails + sqlite_emails)  # Use set to avoid duplicates

# Send emails to each recipient
for recipient_email in all_emails:
    send_html_email(
        smtp_email, 
        smtp_password, 
        recipient_email, 
        subject, 
        html_content, 
        custom_sender_name, 
        custom_sender_email, 
        reply_to=reply_to_email
    )
