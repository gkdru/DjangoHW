from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, get_connection
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User


def send_password_reset_emails(users):
    for user in users:
        subject = "Password Reset Request"
        html_message = render_to_string(
            "password_reset_email_template.html", {"user": user}
        )
        plain_message = strip_tags(html_message)
        from_email = "your-email@example.com"
        to_email = user.email

        print(f"Subject: {subject}")
        print(f"From: {from_email}")
        print(f"To: {to_email}")
        print("Plain text message:")
        print(plain_message)
        print("HTML message:")
        print(html_message)
        print("-" * 50)


def send_reset_emails_view(request):

    users = User.objects.all()
    send_password_reset_emails(users)
    return HttpResponse("Password reset emails sent successfully.")
