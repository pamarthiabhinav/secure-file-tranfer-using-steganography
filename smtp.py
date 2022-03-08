import itertools, threading, time, sys, os, termcolor, smtplib
from termcolor import colored
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename

done = False

sender_email = 'cacdprojectbatch03@gmail.com'
sender_password = 'projectbatch3'


# print colored('world', 'green')

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        os.system('color')
        sys.stdout.write(colored('\rloading ' + c, 'cyan'))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')

def send_mail(subject, text, send_to, files= None):
    send_to = sender_email if not send_to else send_to
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(send_to)
    msg['Subject'] = subject

    with open(text, 'rb') as h:
        text_data = h.read()
        text_data = str(text_data, 'UTF-8')
        msg.attach(MIMEText(text_data, 'plain'))
    for f in files or []:
        with open(f, "rb") as fil: 
            ext = f.split('.')[-1:]
            attachedfile = MIMEApplication(fil.read(), _subtype = ext)
            attachedfile.add_header('content-disposition', 'attachment', filename=basename(f))
            # print(attachedfile)
            msg.attach(attachedfile)
    smtp = smtplib.SMTP(host="smtp.gmail.com", port= 587)
    smtp.ehlo() 
    smtp.starttls()
    smtp.ehlo()
    smtp.login(sender_email,sender_password)
    # smtp.sendmail(sender_email, send_to, msg.as_string())
    smtp.sendmail(sender_email, send_to, msg.as_string())
    smtp.close()


def main(image):
    recipient_emails = list(input("Enter the recipients mail-id seperated by spaces: ").split())
    subject = input("Add email subject: ")
    message = input("Input the message File: ")
    files=['cipher.txt', image]
    t1 = threading.Thread(target=animate)
    t1.start()
    h = ''
    try:
        send_mail(subject, message, recipient_emails, files)
        h = termcolor.colored("Successfully Sent The Mail Buddy", "green")
    except Exception as e:
        h = termcolor.colored("Error In Sending Mail Buddy: " + str(e), "red")
    global done
    done = True
    time.sleep(0.2)
    os.system('color')
    print(h)



