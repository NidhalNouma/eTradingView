from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up)
def send_welcome_email_allauth(request, user, **kwargs):
    print('Sending welcome email', user.email)
    send_welcome_email(user.email, user.email)


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
