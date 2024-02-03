from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_welcome_email(user_email, user_name):
    if user_name.find('@'):
        user_name = user_email.split("@")[0]
    subject = 'Welcome to IsAlgo comunity!'
    html_content = render_to_string('emails/welcome_email.html', {'user_name': user_name})
    email = EmailMessage(subject, html_content, from_email=f"Welcome to IsAlgo! <{settings.EMAIL_HOST_USER}>", to=[user_email])
    email.content_subtype = 'html'  # This is required because default is plain text
    
    try:
        email.send()
    except Exception as e:
        # Handle the exception as needed
        print(f"Error sending email: {e}")