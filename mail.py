import smtplib, ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "abc@xyz.om"  # Enter sender's address
receiver_email = "pqr@xyz.com"  # Enter receiver address
password = "***" #Enter password of sender's id
def mail(initial_accuracy, final_accuracy):
    message = """\
Subject: Best model created from MLOps pipeline
Hello
Hurray!!! Your model's accuracy has been increased from {0}% to {1}%.
This has been achieved by combining the capabilities of ML with DevOps.
Regards
Pranshul's MLOps Pipeline""".format(initial_accuracy, final_accuracy)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)