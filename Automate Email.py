#!/usr/bin/env python
# coding: utf-8

# ### Method 1: Proven works. From: https://www.bilibili.com/video/BV1st4y1B78N

# In[ ]:


import schedule
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail():
    msg = MIMEText("Hi, this is a testing mail. Since I couldn't find the open-up option for SMTP authentication in outlook mail, here's the testing sending from 126 mailbox.", 'html', 'utf-8')
    msg['From'] = formataddr(["Gao, Eden-YD", "ydangao@126.com"])
    msg['Subject'] = "One Sentence A Day"

    server = smtplib.SMTP_SSL("smtp.126.com")
    server.login("ydangao@126.com", "GYMNHNGSDCORYLXJ")
    to = ["1456679221@qq.com", "Eden-YD.Gao@aia.com", "", ""]
    server.sendmail("ydangao@126.com", to, msg.as_string())
    server.quit()
    
mail()


# Method 2: Can't work on scheduling

# In[ ]:


import schedule
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os


# In[22]:


# send our email message 'msg' to our boss
def message(subject="Python Notification",
			text="", img=None, attachment=None):
	
	# build message contents
	msg = MIMEMultipart()
	
	# Add Subject
	msg['Subject'] = subject
	
	# Add text contents
	msg.attach(MIMEText(text))

	# Check if we have anything
	# given in the img parameter
	if img is not None:

		# Check whether we have the
		# lists of images or not!
		if type(img) is not list:
			
			# if it isn't a list, make it one
			img = [img]

		# Now iterate through our list
		for one_img in img:
			
			# read the image binary data
			img_data = open(one_img, 'rb').read()
			
			# Attach the image data to MIMEMultipart
			# using MIMEImage,
			# we add the given filename use os.basename
			msg.attach(MIMEImage(img_data,
								name=os.path.basename(one_img)))

	# We do the same for attachments
	# as we did for images
	if attachment is not None:

		# Check whether we have the
		# lists of attachments or not!
		if type(attachment) is not list:
			
			# if it isn't a list, make it one
			attachment = [attachment]

		for one_attachment in attachment:

			with open(one_attachment, 'rb') as f:
				
				# Read in the attachment using MIMEApplication
				file = MIMEApplication(
					f.read(),
					name=os.path.basename(one_attachment)
				)
			file['Content-Disposition'] = f'attachment;			filename="{os.path.basename(one_attachment)}"'
			
			# At last, Add the attachment to our message object
			msg.attach(file)
	return msg


def mail():
	
	# initialize connection to our email server,
	# we will use gmail here
	smtp = smtplib.SMTP('outlook.office365.com', 995)
	smtp.ehlo()
	smtp.starttls()
	
	# Login with your email and password
	smtp.login('Eden-YD.Gao@aia.com', 'Dangle0129!')

	# Call the message function
	msg = message("Good!", "Hi there!"
				#,r"C:\Users\Dell\Downloads\Garbage\Cartoon.jpg"
				#,r"C:\Users\Dell\Desktop\slack.py"
                 )
	
	# Make a list of emails, where you wanna send mail
	to = ["1456679221@qq.com"]

	# Provide some data to the sendmail function!
	smtp.sendmail(from_addr="Eden-YD.Gao@aia.com",
				to_addrs=to, msg=msg.as_string())
	
	# Finally, don't forget to close the connection
	smtp.quit()


#schedule.every(2).seconds.do(mail)
#schedule.every(10).minutes.do(mail)
#schedule.every().hour.do(mail)
#schedule.every().day.at("17:24").do(mail)
#schedule.every(5).to(10).minutes.do(mail)
#schedule.every().monday.do(mail)
#schedule.every().wednesday.at("13:15").do(mail)
#schedule.every().minute.at(":17").do(mail)

#while True:
#	schedule.run_pending()
#	time.sleep(1)


# In[25]:


message(subject="Python Notification",
			text="", img=None, attachment=None)

schedule.every().day.at("17:34").do(mail)

