import smtplib
from twilio.rest import Client

def send_email_notification(email: str, message: str):
    # Simulamos envío de email
    print(f"Enviando email a {email}: {message}")

def send_sms_notification(phone: str, message: str):
    # Simulamos envío de SMS
    print(f"Enviando SMS a {phone}: {message}")