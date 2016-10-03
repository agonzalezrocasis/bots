#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

"""
with open('msg.txt') as fp:
    msg = MIMEText(html, fp.read())
"""
"""
msg = MIMEText('<h5 style="color: gray;">Hi there! I am @LobyBot</h5>', 'html')

print('Send email')

msg['Subject'] = 'Greeting from @LobyBot'
msg['From'] = 'betbatesc@gmail.com'
msg['To'] = 'agonzalez@rocasis.mx'

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login('betbatesc@gmail.com', '2008090274')
s.send_message(msg)
s.quit()

print('Email sent')
"""

def send_message_image():
    msg = MIMEMultipart()

    print('Send email')

    msg['Subject'] = 'Greeting from @LobyBot'
    msg['From'] = 'betbatesc@gmail.com'
    msg['To'] = 'agonzalez@rocasis.mx'
    msg.preamble = '@LobyBot'

    with open('bot.png', 'rb') as fp:
        img = MIMEImage(fp.read())

    msg.attach(img)

    print('Image attached')

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login('betbatesc@gmail.com', '2008090274')
    s.send_message(msg)
    s.quit()
    print('Email sent')

def send_message_html():
    msg = MIMEMultipart('alternative')

    print('Send email')

    msg['Subject'] = 'Greeting from @LobyBot'
    msg['From'] = 'betbatesc@gmail.com'
    msg['To'] = 'agonzalez@rocasis.mx'

    text = 'Hi there!'

    html = '<h4 style="color: gray;">Hi there! I am @LobyBot</h4>'

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login('betbatesc@gmail.com', '2008090274')
    s.send_message(msg)
    s.quit()
    print('Email sent')

def send_message_html_image():
    msg = EmailMessage()



if __name__ == '__main__':
    send_message_html()
    msg['Subject'] = 'Greeting from @LobyBot'
    msg['From'] = 'betbatesc@gmail.com'
    msg['To'] = 'agonzalez@rocasis.mx'
    msg.set_content("""\
Salut!

Cela ressemble à un excellent recipie[1] déjeuner.

[1] http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718

--Pepé
""")

# Add the html version.  This converts the message into a multipart/alternative
# container, with the original text message as the first part and the new html
# message as the second part.
asparagus_cid = make_msgid()
msg.add_alternative("""\
<html>
  <head></head>
  <body>
    <p>Salut!<\p>
    <p>Cela ressemble à un excellent
        <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718>
            recipie
        </a> déjeuner.
    </p>
    <img src="cid:{asparagus_cid}" \>
  </body>
</html>
""".format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
# note that we needed to peel the <> off the msgid for use in the html.

# Now add the related image to the html part.
with open("roasted-asparagus.jpg", 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                     cid=asparagus_cid)

# Make a local copy of what we are going to send.
with open('outgoing.msg', 'wb') as f:
    f.write(bytes(msg))

# Send the message via local SMTP server.
with smtplib.SMTP('localhost') as s:
    s.send_message(msg)
