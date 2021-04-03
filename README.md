# Python code to link to GOV.uk Notify

This python script was created to use with the Open source
robotic process automation program (RPA) AutoHotKey. It uses
the command line arguements as inputs. Hence, it can be used by
any program, or even typed manually into the command line to send
SMS messages, emails or letters via the GOV.uk Notify service

You need to sign up to GOV.uk first and then get an API-key and 
template ID. You need to create templates with the below 'personalisations'.

Once you have them the following arguements are taken:

Arguements:

1. "SMS", "email" or "letter" to inform what communication method is required
2. AKI_key
3. template ID

SMS:

4. mobile number in format 07123456789
5. message

Email:

4. email address
5. subject
6. message

letter:

4. address, using semi-colon ";" to denote new lines
5. from
6. heading
7. body

To make into an executable, make sure you have pyInstaller installed.
Then go into the folder with your code and run:

pyinstaller --onefile .\GovNotify.py

The dist folder will then hold the exe

								 
