#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Employers():
    __counter = 0

    def __init__(self, counter, name, email, password,
                 dob, phnum, age, status):
        type(self).__counter += counter + 1
        self.counter = Employers.__counter
        self.name = name
        self.__email = email
        self.__password = password
        self.dob = dob
        self.phnum = phnum
        self.age = age
        self.status = status

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @staticmethod
    def counter_return():
        return Employers.__counter

    def employers_forget_details(self):
        message = "Dear {},\n\n\nWe hope this message finds you well.\nIt appears you may have forgotten your account details for Jobify-Tech. Not to worry-we're here to help you regain access to your account.\nBelow are your account details: \n\n".format(self.name)
        message += "        Password: {}\n\n".format(self.password)
        message += "        Employer number: {}".format(self.counter)

        subject = "Employer Details"
        sender_email = "jobify.tech@gmail.com"
        sender_password = "cg2LvSwJ46T9j3P7"
        recipient_email = self.email

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        smtp_server = "smtp-relay.brevo.com"
        smtp_port = 587

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()
            print("Email sent successfully.")
        except Exception as e:
            print("An error occurred while sending the email:", e)

        print("Email details sent to employer.")
