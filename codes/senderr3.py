import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

def send_html_email(
    sender_email, 
    sender_password, 
    recipient_email, 
    subject, 
    html_file_path, 
    display_name=None, 
    reply_to=None
):
    # Set up the MIME
    email_message = MIMEMultipart()
    
    # If display_name is provided, format the "From" field
    if display_name:
        email_message['From'] = formataddr((display_name, sender_email))
    else:
        email_message['From'] = sender_email
    
    # Add recipient and subject fields
    email_message['To'] = recipient_email
    email_message['Subject'] = subject
    
    # If a custom reply-to is provided, set it in the headers
    if reply_to:
        email_message['Reply-To'] = reply_to

    # Read the HTML content from the external file
    with open(html_file_path, 'r') as file:
        html_content = file.read()
    
    # Attach the HTML message
    email_message.attach(MIMEText(html_content, 'html'))
    
    server = None  # Initialize server to None
    
    try:
        # Connect to the server
        server = smtplib.SMTP('mail.americanestateproperties.com', 587)
        server.starttls()  # Enable security
        
        # Login
        server.login(sender_email, sender_password)
        
        # Send the email
        server.send_message(email_message)
        
        print("HTML email sent successfully!")
    
    except Exception as e:
        print(f'Failed to send email. Error: {e}')
    
    finally:
        if server is not None:
            server.quit()

# Usage example:
sender_email = "agent@americanestateproperties.com"
sender_password = "EriggA200@@"  # Use the app password if 2FA is enabled
recipient_email = "danieluka452@gmail.com"
subject = "Welcome to Our Service!"
html_file_path = "codes/danielmess.html"  # Path to the HTML file

# Display name, reply-to email (optional)
display_name = "VERILY"
reply_to_email = "reply_to@example.com"

send_html_email(
    sender_email, 
    sender_password, 
    recipient_email, 
    subject, 
    html_file_path, 
    display_name=display_name, 
    reply_to=reply_to_email
)
