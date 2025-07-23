from datetime import datetime
import smtplib
import pandas
import random

# MailHog container is used to test sending and receiving
# for gmail we need to set up a specific password for the app in the google account's security
# COMMON SMTP ADDRESSES
# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com

SMTP_SERVER_ADDR = "localhost"
SMTP_SERVER_PORT = 1025
SENDER_EMAIL = "somesender@mail.com"
SENDER_EMAIL_PASS = "anypass"
BIRTHDAYS_FILE = "../resources/birthdays.csv"
RANDOM_MESSAGE = f"../resources/letter_templates/letter_{random.randint(1, 3)}.txt"
TODAY = datetime.now()

def main():
    today_tuple = (TODAY.month, TODAY.day)

    birthdays_df = pandas.read_csv(BIRTHDAYS_FILE)
    birthdays_dict = { (row["month"], row["day"]) : row for (index, row) in birthdays_df.iterrows() }

    if today_tuple in birthdays_dict:
        entry = birthdays_dict[today_tuple]

        with open(RANDOM_MESSAGE) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", entry["name"])
            subject = "Subject: Happy Birthday!\n\n"

        with smtplib.SMTP(SMTP_SERVER_ADDR, port=SMTP_SERVER_PORT) as connection:
            # TLS is not available for local testing with MailHog
            # connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PASS)
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=entry["email"], msg=f"{subject}{contents}")


if __name__ == "__main__":
    main()