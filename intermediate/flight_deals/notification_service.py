import smtplib

class NotificationService:

    def __init__(self):
        """
        MailHog container is used to test sending and receiving
        """
        self.smtp_server_address = "localhost"
        self.smtp_server_port = 1025
        self.smtp_sender = "flightclub@flightclub.com"
        self.smtp_sender_pass = "anypass"

    def send_email(self, destination, message):
        for user_mail in destination:
            with smtplib.SMTP(self.smtp_server_address, port=self.smtp_server_port) as connection:
                connection.login(user=self.smtp_sender, password=self.smtp_sender_pass)
                connection.sendmail(from_addr=self.smtp_sender, to_addrs=user_mail, msg=message)