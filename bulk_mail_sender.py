import smtplib as s
ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()


# ENTER YOUR EMAIL ID AND PASSWORD:-
ob.login('samplemail@gmai.com', 'enter your password here')

# ENTER YOUR EMAIL SUBJECT HERE:-
subject = "enter your subject here"


# ENTER YOUR FULL MESSAGE HERE:-
body = "enter your full message here"

massage = "subject:\n\n{}".format(subject, body)


# ENTER THE EMAIL ADDRESSES HERE WHOM YOU WANT TO SEND MAIL:-
listadd = ['samplemail1@gmail.com',
           'samplemail2@gmail.com',
           'samplemail3@gmail.com',
           'samplemail4@gmail.com']

ob.sendmail('samplemail@gmail.com', listadd, massage)
print("Email has been send.")

ob.quit()
