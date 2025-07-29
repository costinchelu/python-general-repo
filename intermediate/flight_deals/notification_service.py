import smtplib

class NotificationService:
    """
    MailHog container is used to test sending and receiving
    """

    def __init__(self):
        self._smtp_server_address = "localhost"
        self._smtp_server_port = 1025
        self._smtp_sender = "flightclub@flightclub.com"
        self._smtp_sender_pass = "anypass"

    def send_email(self, destination, message):
        for user_mail in destination:
            with smtplib.SMTP(self._smtp_server_address, port=self._smtp_server_port) as connection:
                connection.login(user=self._smtp_sender, password=self._smtp_sender_pass)
                connection.sendmail(from_addr=self._smtp_sender, to_addrs=user_mail, msg=message)