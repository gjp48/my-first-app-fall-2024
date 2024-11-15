# this is the app/email_service.py file...

# LOCAL DEV (ENV VARS)

import os
from dotenv import load_dotenv

load_dotenv() # looks in the ".env" file for env vars

SENDGRID_SENDER_ADDRESS = os.getenv("SENDGRID_SENDER_ADDRESS")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")


from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# HELPER FUNCTION:

def send_email_with_sendgrid(recipient_address=SENDGRID_SENDER_ADDRESS,
                             subject="[Shopping Cart App] Testing 123",
                             html_content="<p>Hello World</p>"
                            ):
    """Sends an email to the given recipient address.

        Params:
            recipient_address (str): The email address of the recipient.

            subject (str): The subject of the email.

            html_content (str): The content of the email. Can pass a string formatted as HTML.
    """
    print("SENDING EMAIL TO:", recipient_address)
    #print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    # always send from the sender, but allow us to customize the recipient by passing it in to the function as a parameter
    message = Mail(from_email=SENDGRID_SENDER_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        #print(response.body)
        #print(response.headers)
        print("Email sent successfully!")
    except Exception as err:
        print(f"Error sending email:")
        print(type(err))
        print(err)

# SEND EXAMPLE EMAIL:

send_email_with_sendgrid(html_content="Hello. Tuesday Night")
