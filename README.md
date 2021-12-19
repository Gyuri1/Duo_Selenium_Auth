# Duo_Selenium_Auth

This script provides a python 3 Selenium based authentication against Duo SAML protected Service Provider Application.

Use this way:

1. Download and install the Selenium based browser driver based on this:
   https://selenium-python.readthedocs.io/  
   
   I tested with Chrome browser. 

2. Run this script with the necessary parameters, like domain (without https://), username and password like this way:
```
python3 Duo_selenium_auth.py sp.duoprotected.com username@domain.net BigSecretPassword  
Sending username...  
Sending password...    
```
Otherwise script will ask them:  
```
python3 Duo_selenium_auth.py   
Duo SAML protected Service Provider (SP) URL (WITHOUT https://): sp.duoprotected.com  
Username: username@domain.net  
Password: BigSecretPassword  
Sending username...  
Sending password...   
```
