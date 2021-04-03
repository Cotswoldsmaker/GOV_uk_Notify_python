# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 07:02:31 2021

@author: mark.bailey
"""

import sys
#from time import sleep

from notifications_python_client.notifications import NotificationsAPIClient

response = 'Wrong initial arguement'

try:
    if sys.argv[1] == 'SMS':
        notifications_client = NotificationsAPIClient(sys.argv[2])  # API_key from GOV.uk Notify
        
        response = notifications_client.send_sms_notification(
            template_id= sys.argv[3],                               # This is the SMS template ID on GOV.uk Notify
            phone_number= sys.argv[4],                             # Mobile number in format 01234 567890
        
            personalisation={
                'message': sys.argv[5],                             # The message to send via SMS
            }
        )
            
    elif sys.argv[1] == 'email':
        notifications_client = NotificationsAPIClient(sys.argv[2])  # API_key from GOV.uk Notify
        
        response = notifications_client.send_email_notification(
            template_id= sys.argv[3],                               # This is the email template ID on GOV.uk Notify
            email_address= sys.argv[4],                             # email address
            
            personalisation={
                'subject': sys.argv[5],
                'message': sys.argv[6],
            }
        )
        
    elif sys.argv[1] == 'letter':
        notifications_client = NotificationsAPIClient(sys.argv[2])  # API_key from GOV.uk Notify
        
        addressLines = sys.argv[4].split(';')
        
        personalisationT={                        
            'from' : sys.argv[5],
            'heading' : sys.argv[6],
            'body' : sys.argv[7],
        }
        
        for index, line in enumerate(addressLines):
            lineNr = index + 1
            personalisationT['address_line_' + str(lineNr)] =line
       
        response = notifications_client.send_letter_notification(template_id=sys.argv[3], personalisation = personalisationT)

except:
    print('unsuccessful')
    sys.exit(0)
else:
    print(response)
    sys.exit(0)
