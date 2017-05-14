####--------------------------------------------------------
#### Purpose:         Send a text message of the local
####                  IP address to phone provider or
####                  e-mail account. Requires a gmail account.
####
####--------------------------------------------------------
import time
import commands
import re
import smtplib
import socket

####--[Start of Custom Items]

server = 'smtp.gmail.com'					# smtp server address
server_port = '587' 						# port for smtp erver
username = 'XXXXXXX@gmail.com'				# e-mail login
password = 'YourPassword'					# e-mail password
sendtoaddr = '10DigitNumber@gateway.net' 	# e-mail address or phone to send txt msg to - If using a phone number, use the addresses from the following,
											# inserting your phone number where appropriate.

# Cell Phone Service Provider Addresses

# Alltel: phonenumber@message.alltel.com
# AT&T: phonenumber@txt.att.net
# T-Mobile: phonenumber@tmomail.net
# Virgin Mobile: phonenumber@vmobl.com
# Sprint: phonenumber@messaging.sprintpcs.com
# Verizon: phonenumber@vtext.com
# Nextel: phonenumber@messaging.nextel.com
# US Cellular: phonenumber@mms.uscc.net


####-- [End of Custom Items]


fromaddr = username
toaddr = sendtoaddr
rpiname = (socket.gethostname())
message = rpiname +' RPi\'s address: ' #message that is sent
time.sleep(5)

#extract the ip address (or addresses) from ipinfo.io/ip

ips = re.findall( r'[0-9]+(?:\.[0-9]+){3}', commands.getoutput("curl http://ipinfo.io/ip"))

message += str(ips)
headers = ["From: " + fromaddr,
           "To: " + toaddr,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)

server = smtplib.SMTP(server + ':' + server_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddr, headers + "\r\n\r\n" +  message)
server.quit()
