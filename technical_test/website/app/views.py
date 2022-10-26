from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import smtplib
import ssl
import numpy as np
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from math import ceil
from . import models
from .models import user

name = ''
email = ''
password = ''
otp = 0

def reg(request):
        return render(request, 'registration.html')

# Function that verifies the user through its email otp
def reg_verification(request):
    global otp
    global name
    global email
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        contact = request.POST.get('contact')
        otp = np.random.randint(111111, 999999)
        smtp_server = "smtp.outlook.com"
        port = 587  # For starttls# outlook PORT = 587
        sender_email = "21mci1033@cuchd.in"     # Account through which the user will receive the otp. 
        sender_password = '*******' # Password of the account
        receiver_email = email
        subject = 'OTP Verification'
        message = """
                    """ + subject+""": OTP Verification\n
                    Hello """+ name + """\n
                    You have registered for the fonestore.com.\n
                    PLease verify your account.\n
                    Your OTP is {}.""".format(otp)

        # Create a secure SSL context
        context = ssl.create_default_context()
        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls(context=context)  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)

        except Exception as e:
            # Print any error messages to stdout
            messages.error(request, "Invalid Email Address")

        finally:
            server.quit()

        context = {
            email : email
        }
        return render(request, 'otp_verification.html', context)

# Function that verify the OTP through email
def verify(request):
    i = request.POST.get("otp")
    if int(i) == int(otp):
        person = models.user(name=name, email=email, password=password)
        person.save()
        content = {
            name: name,
        }
        return render(request, 'home.html', content)
    else:
        messages.error(request, "Wrong OTP")
        return render(request, 'login.html')

# Function that leads to login page
def login(request):
    return render(request, 'login.html')

# Function that verifies the login id and password
def login_validation(request):
    id = request.POST.get('email')
    pas = request.POST.get('password')
    person = authenticate(email=id, password=pas)

    if person is not None:
        login(request, person)
        messages.success(request, "Login successfully")
        content = {
            name: person
        }
        return render(request, 'home.html', content)

    else:
        messages.error(request, 'Invalid emailID or Password')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

# Function that leads to the html page of contact us
def contact_us(request):
    return render(request, 'contact_us.html')


def query(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get('message')
    smtp_server = "smtp.outlook.com"
    port = 587  # For starttls# outlook PORT = 587
    sender_email = "21mci1033@cuchd.in" # Account through which user will receive the confirmation about the contact us page 
    sender_password = '*******'         # Password of the account
    receiver_email = email
    subject = 'OTP Verification'
    message = """
                        Thank you for contacting us\n Our team will try to solve your query within 24 hrs\n
                        Your Query was : \n
                        Query About the Application\n
                        Subject: """ + subject + """\n
                        message: {}.""".format(message)

    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        messages.error(request, "Invalid Email Address")

    finally:
        server.quit()

    messages.success("We have recorded your Query ")
    return redirect("")
