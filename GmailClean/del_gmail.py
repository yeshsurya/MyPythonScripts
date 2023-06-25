import imaplib

# IMAP server connection details
imap_server = 'imap.gmail.com'
username = 'yeshsurya@gmail.com'
password = ''

# List of sender emails
sender_emails = ['yamini@strategink.co.in','nimfupdates@campaign1.nipponindia.email', 'noreply@indusind.com','info@tran.india-furniture.co.in','noresponse@hdfcfund.com','no-reply@flash.mylio.com'
                 ,'noreply@nykaa.com','newsletter@etenergyworld.com','info@naukri.com','no-reply@invest.hdfcsecmail.com','info@shine-mails.com'
                 ,'elearn@quantsapp.in','notifications@github.com','yonosbi@alerts.sbi.co.in','info@zipcodewilmington.com','mail-comsol-in@comsol.co.in','info@mail-lionsgateplay.com','alert@info.bigbasket.com',
                 'Bitcoin-Blockchain-Technology-Meetup-list@email.meetup.com','updates@goldenpi.com','info@alerts.foundit.in','news@mail.maxfashion.in'
                 ,'mf@ppfas.in','sap-jobnotification@noreply12.jobs2web.com','info@hirist.com','info@update.nurserylive.com','aws-marketing-email-replies@amazon.com','do_not_reply@mailersp2.binance.com',
                 'RMG@1105newsletters.com','noreply@zen-makemytrip.com','retailproducts@kotak.in','no-reply@geeksforgeeks.org','updates@goldenpi.com','no-reply@screener.in','freebsd-announce+help@freebsd.org'
                 ,'info@mailer.smallcase.com','weekly.news@horoscopefree.com','info@mailer.netflix.com','no-reply@primevideo.com','newsletters@audible.in','shop@email.stackcommerce.com','reminders@facebookmail.com'
                 ,'info@hirist.com','hello@medium.com','shop@email.stackcommerce.com','messages-noreply@linkedin.com','learn@email1.asana.com','info@mailer.netflix.com','hello@info.etmoney.com'
                 ,'newsletters@nl.technologyadvice.com','calendar-notification@google.com','noreply@digest.groww.in','microsoft.start@email2.microsoft.com','team@hired.com',
                 'founder@ambitionbox.com','noreply@eduonix.com','easyequity@info.kotaksecurities.co.in','newsletter@em.geekmailz.com','inceptionprogram@nvidia.com','newsletters@inform.wtwhmedia.com',
                 'info@newsletters.analyticsvidhya.com','email@engage.redhat.com','news@m.market.envato.com','Impinfo@updates.airtel.com','services@custcomm.icicibank.com','newsletter@javacodegeeks.com','dailybrief694@substack.com',
                 'noreply@groww.in','naukrialerts@naukri.com','help@sensibull.com','rkumar@strategink.co.in','newsletter@notifications-economictimes.com','messaging-digest-noreply@linkedin.com','customer-success@mirantis.com','mailers@marketing.goindigo.in',
                 'no-reply@hello.redis.com','newsletter@reply.agoda-emails.com','eply@et.oreilly.com','ivan@mail.notion.so','hello@chess.com','VSLive@1105info.com','info@alerts.foundit.in','informations@hdfcbank.net','no-reply@invest.hdfcsecmail.com']

# Connect to the IMAP server using SSL
imap = imaplib.IMAP4_SSL(imap_server)

# Login to the server
imap.login(username, password)

# Select the mailbox/folder where the emails are located
mailbox = r"INBOX"
mailboxes=['"[Gmail]"','"[Gmail]/All Mail"','Updates']
imap.select(mailbox)
for i in imap.list()[1]:
    l = i.decode().split(' "/" ')
    print(l[0] + " = " + l[1])

for mailbox in mailboxes:
    print(f' *********** Searching in mail box {mailbox} **************')

    # Iterate over each sender email
    for sender_email in sender_emails:
        print(f"Deleting emails from: {sender_email}")

        # Search for emails from the specific sender
        search_criteria = f'(FROM "{sender_email}")'
        result, data = imap.search(None, search_criteria)

        if result == 'OK':
            # Get the list of email IDs from the search results
            email_ids = data[0].split()

            if email_ids:
                print("Emails to be deleted:")

                # Iterate over each email ID and delete the email
                for email_id in email_ids:
                    # Mark the email for deletion
                    imap.store(email_id, '+FLAGS', '\\Deleted')

                    # Fetch the email headers to display information (optional)
                    result, email_data = imap.fetch(email_id, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
                    if result == 'OK':
                        subject = email_data[0][1].decode('utf-8')
                        print(f"Subject: {subject}")

                # Permanently delete the emails marked for deletion
                imap.expunge()
            else:
                print('No emails found from the specified sender.')

# Logout and close the connection
imap.logout()

