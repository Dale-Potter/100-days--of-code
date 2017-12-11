#EmailerTradingNews

import smtplib
from smtplib import SMTPException

sender = "@hotmail.com"
receiver = "@hotmail.co.uk"
passwd = "0000"
mail_server = 'smtp-mail.outlook.com'

msg = "\r\n".join([
  "From: Sender@hotmail.com",
  "To: Reciever@hotmail.co.uk",
  "Subject: Git ",
  "",
  "Message part"
  ])
try:

	server = smtplib.SMTP(mail_server, 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(sender, passwd)
	server.sendmail(sender, receiver, msg)
	server.close()

except SMTPException:
    print('Error')