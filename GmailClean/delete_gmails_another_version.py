import os
import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Define the sender's email address
sender_email = "nimfupdates@campaign1.nipponindia.email"

def authenticate_gmail():
    """
    Authenticates the user and returns the Gmail service object.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        creds = build_service_account_creds()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

def build_service_account_creds():
    """
    Builds the service account credentials using app password.
    """
    from google.oauth2.credentials import Credentials

    # Enter your app password details here
    app_email = "yeshsuya@gmail.com"
    app_password = ""

    creds = Credentials.from_authorized_user_info(
        {
            "client_id": app_email,
            "client_secret": app_password,
            "token_uri": "https://accounts.google.com/o/oauth2/token",
            "scopes": ["https://www.googleapis.com/auth/gmail.modify"],
        }
    )
    creds.refresh(Request())
    return creds

def delete_emails_from_sender(service, sender_email):
    """
    Deletes emails from a specific sender in Gmail.
    """
    # Search for emails from the specified sender
    query = f"from:{sender_email}"
    response = service.users().messages().list(userId='me', q=query).execute()
    messages = response.get('messages', [])
  
    if not messages:
        print('No emails found from the specified sender.')
        return

    # Delete each email found
    for message in messages:
        service.users().messages().delete(userId='me', id=message['id']).execute()
        print(f"Deleted email with ID: {message['id']}")

# Authenticate Gmail and get the service object
service = authenticate_gmail()

# Delete emails from the specified sender
delete_emails_from_sender(service, sender_email)
