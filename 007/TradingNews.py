# Import all the modules for web scraping and Emailing
from lxml import html
import requests
import smtplib
from smtplib import SMTPException

# Declaring all variables for the email accounts used
sender = "sender@hotmail.com"
receiver = "reciever@hotmail.co.uk"
passwd = "0000"
mail_server = 'smtp-mail.outlook.com'

# Web scrape Crypto Coins News
page = requests.get('https://www.cryptocoinsnews.com/')
tree = html.fromstring(page.content)

# Specify what data needs storing from site and save to 'news;
news = tree.xpath('//div[@class="entry-title"]/text()')

#Replace any characters that SMTP cant read 
string = '\n'.join(news)
string = string.replace('‘','-')
string = string.replace('’','-')

#Message that will be sent (Formatt is very important)
msg = "\r\n".join([
  "From: sender@hotmail.com",
  "To: reciever@hotmail.co.uk",
  "Subject: Todays Crypto Currency News",
  "", string ])
  
#Try and except user for error handling, gives feedback on whether the email was succesful or not 
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