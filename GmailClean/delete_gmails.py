import imaplib
import smtplib, time, imaplib
import email

def delete_emails(username, password, folder_name, search_criteria):
  """Deletes emails from a Gmail folder.

  Args:
    username: The Gmail username.
    password: The Gmail password.
    folder_name: The name of the Gmail folder to delete emails from.
    search_criteria: The search criteria to use to find the emails to delete.

  Returns:
    The number of emails deleted.
  """

  imap = imaplib.IMAP4_SSL("imap.gmail.com")
  imap.login(username, password)
  print(imap.list())
  imap.select(folder_name)

  status, messages = imap.search(None, 'From','"nimfupdates@campaign1.nipponindia.email"')
  if status == "OK":
    num_deleted = 0
    print("The following emails will be deleted:")
    for message_id in messages:
      print(message_id)
      response = input("Do you want to proceed? (y/N): ")
      if response == "y":
        imap.store(message_id, '+FLAGS', '\\Deleted')
        num_deleted += 1

    imap.expunge()

    return num_deleted
  else:
    return 0

if __name__ == "__main__":
  username = "yeshsurya@gmail.com"
  password = ""
  folder_name = "INBOX"
  search_criteria = "is:unread"

  search_criterias = ['(FROM "nimfupdates@campaign1.nipponindia.email")',
                      ]

  num_deleted = delete_emails(username, password, folder_name, search_criteria[0])
  print("Deleted {} emails.".format(num_deleted))

  #info@goelasf.in
