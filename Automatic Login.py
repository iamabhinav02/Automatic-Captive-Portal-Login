import sys
from selenium import webdriver
driver = webdriver.Chrome()

try: 
	driver.get("") # Fill in the url address of your portal
except:
	sys.exit(0)

username = driver.find_element_by_name("username")
username.clear()

password = driver.find_element_by_name("password")
password.clear()

username.send_keys("") # your username
password.send_keys("") # your password

driver.find_element_by_id("loginbutton").click()

print("Logged In.")

driver.close()