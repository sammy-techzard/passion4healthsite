from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    try:
        send_mail(
            'Test Email',
            'This is a test email to check the email configuration.',
            'info@passion4health.org',  # Replace with your "from" email
            ['nisammy40@gmail.com'],  # Replace with recipient's email
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully.")
    except Exception as e:
        return HttpResponse(f"Error sending email: {str(e)}")
