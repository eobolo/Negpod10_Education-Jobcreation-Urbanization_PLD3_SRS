#!/usr/bin/python3
"""
This is our class

Employee that creates

an Employee class

and has some nice

methods
"""


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colours import Color


class Employees():
    __counter = 0

    def __init__(self, counter, name, email, password,
                 dob, phnum, age, status, jobtitle):
        type(self).__counter += counter + 1   
        self.counter = Employees.__counter
        self.__name = name
        self.__email = email
        self.__password = password
        self.__dob = dob
        self.__phnum = phnum
        self.__age = age
        self.status = status
        self.__jobtitle = self.adjustjobtitle(jobtitle)
        self.__jobsaved = []

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, value):
        self.__dob = value

    @property
    def phnum(self):
        return self.__phnum

    @phnum.setter
    def phnum(self, value):
        self.__phnum = int(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = int(value)

    @property
    def jobtitle(self):
        return self.__jobtitle

    @staticmethod
    def counter_return():
        return Employees.__counter

    @property
    def jobsaved(self):
        return self.__jobsaved

    @jobsaved.setter
    def jobsaved(self, jobname):
        self.__jobsaved.append(jobname)

    def adjustjobtitle(self, job_name):
        job_names = job_name.split(sep=" ")
        job = ""
        for i in range(len(job_names)):
            if  i == len(job_names) - 1:
                job += job_names[i].capitalize()
                break
            elif i != len(job_names) - 1:
                job += job_names[i].capitalize() + " "
        print(job)
        return job

    def employees_forget_details(self):
        message = "Dear {},\n\n\nWe hope this message finds you well.\nIt appears you may have forgotten your account details for Jobify-Tech. Not to worry-we're here to help you regain access to your account.\nBelow are your account details: \n\n".format(self.name)
        message += "        Password: {}\n\n".format(self.password)
        message += "        Employee number: {}".format(self.counter)

        subject = "Employee Details"
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
            print(Color.GREEN + "Email sent successfully."+ Color.RESET)
        except Exception as e:
            print(Color.RED +"An error occurred while sending the email:", e + Color.RESET)

        print(Color.GREEN +"Email details sent to employee."+ Color.RESET)
