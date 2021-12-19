# Duo Selenium based Authentication
#
# Modified: Dec 19, 2021
#

from selenium import webdriver
from time import sleep
import sys

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_next_arg(prompt):
    try:
        return next(argv_iter)
    except StopIteration:
        return input(prompt)


if __name__ == '__main__':
    # Configuration and information about objects to create.
    argv_iter = iter(sys.argv[1:])
    sp_url=get_next_arg('Duo SAML protected Service Provider (SP) URL (WITHOUT https://): ')
    idp_username=get_next_arg('Username: ')
    idp_password=get_next_arg('Password: ')

    # Open Browser with Selenium 
    driver = webdriver.Chrome()
    driver.get("https://"+sp_url)

    # Wait for input field
    element_present = EC.presence_of_element_located((By.XPATH, '//input'))
    try:
        WebDriverWait(driver, 7).until(element_present)
    except TimeoutException:
        print("Timeout")

    username_field = driver.find_element(By.XPATH, "//input") 

    print("Sending username...") 
    username_field.send_keys(idp_username)
    username_field.send_keys(Keys.RETURN)
    
    # Wait for web page
    driver.implicitly_wait(2)

    print("Sending password...")    
    passw_field = driver.find_element(By.NAME, "password") 
    passw_field.send_keys(idp_password)
    passw_field.send_keys(Keys.RETURN)
