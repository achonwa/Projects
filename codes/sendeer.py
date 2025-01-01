import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_html_email(sender_email, sender_password, recipient_email, subject, html_file_path):
    # Set up the MIME
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = recipient_email
    email_message['Subject'] = subject
    
    # Read the HTML content from the external file
    with open(html_file_path, 'r') as file:
        html_content = file.read()
    
    # Attach the HTML message
    email_message.attach(MIMEText(html_content, 'html'))

    server = None  # Initialize server to None
    
    try:
        # Connect to the server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        #server.starttls()  # Enable security
        
        # Login
        server.login(sender_email, sender_password)
        
        # Send the email
        server.send_message(email_message)
        
        print("HTML email sent successfully!")
    
    except Exception as e:
        print(f'Failed to send email. Error: {e}')
    
    finally:
        if server is not None:  # Only quit if server was initialized
            server.quit()

# Usage example:
sender_email = "danielachonwa452@gmail.com"
sender_password = "zjhnbcuzwxjsetjg"
recipient_email = "julimohz@gmail.com"
subject = "Welcome to Our Service!"
html_file_path = "codes/danielmess.html"  # Path to the HTML file

send_html_email(sender_email, sender_password, recipient_email, subject, html_file_path)
