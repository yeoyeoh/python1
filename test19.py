##06-14##
##메일로 보내기##

import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "yeoyeohg@gmail.com" # gmail address
gmail_pwd = "as95@as97@" # gmail password

def send_gmail(to, subject, text, attach):      #함수 이용하여 메일내용 보내기
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()


hap, i = 0, 0

for i in range(1, 101):
    if i %3 == 0:
        continue

    hap = hap +i

print("1~100의 합계(3의 배수 제외) : %d" % hap)

send_gmail("yeoyeoh@naver.com", "메일보내기", hap)