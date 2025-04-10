import smtplib

my_email = ""  # Replace with your actual email address
password = ""  # Replace with your actual password

connection = smtplib.SMTP("smtp.gmail.com", 587)

connection.starttls()  # Secure the connection
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="e.prisecarudiana@gmail.com ",
    msg="Subject:Hello\n\nThis is the body of the email."
)
connection.close()