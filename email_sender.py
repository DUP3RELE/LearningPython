import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Dupciorol Dupaczyński'
email['to'] = 'fox90804@gmail.com'
email['subject'] = 'Hello there.'

email.set_content('bober kurwa')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('*********@gmail.com', '*************')
  smtp.send_message(email)
  print('all good!')