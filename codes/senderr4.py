import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

def send_html_email(
    smtp_email, 
    smtp_password, 
    recipient_email, 
    subject, 
    html_file_path, 
    custom_sender_name, 
    custom_sender_email, 
    reply_to=None
):
    # Set up the MIME
    email_message = MIMEMultipart()
    
    # Set custom "From" field with display name and custom sender email
    email_message['From'] = formataddr((custom_sender_name, custom_sender_email))
    email_message['To'] = recipient_email
    email_message['Subject'] = subject
    
    # Set "Reply-To" field if provided
    if reply_to:
        email_message['Reply-To'] = reply_to

    # Read the HTML content from the external file
    #with open(html_file_path, 'r') as file:
        #html_content = file.read()
    
    # Attach the HTML message
    email_message.attach(MIMEText(html_file_path, 'plain'))
    
    server = None  # Initialize server to None
    
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('mail.americanestateproperties.com', 587)
        server.starttls()  # Enable security
        
        # Login with the actual sender email and password for authentication
        server.login(smtp_email, smtp_password)
        
        # Send the email using smtp_email for authentication but with a custom "From" header
        server.sendmail(smtp_email, recipient_email, email_message.as_string())
        
        print("HTML email sent successfully with custom sender info!")
    
    except Exception as e:
        print(f'Failed to send email. Error: {e}')
    
    finally:
        if server is not None:
            server.quit()

# Usage example:
smtp_email = "agent@americanestateproperties.com"
smtp_password = "EriggA200@@"  # Use an app password if 2FA is enabled
recipient_email = "danieluka452@gmail.com"
subject = "VERIFY NOW!"
html_file_path = "This is a demo trial message"  # Path to the HTML file

# Custom sender name, custom sender email (different from smtp_email), and optional reply-to email
custom_sender_name = "BITCOIN"
custom_sender_email = "trial@mentordhnd.com"  # Masked email that the receiver will see
reply_to_email = "anothertrial@mmmetr.com"  # Optional reply-to email

send_html_email(
    smtp_email, 
    smtp_password, 
    recipient_email, 
    subject, 
    html_file_path, 
    custom_sender_name, 
    custom_sender_email, 
    reply_to=reply_to_email
)
