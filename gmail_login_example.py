from selenium import webdriver
import time
import stdiomask

# Enter your gmail credentials
username = input("Enter your gmail user id: ")

# In this example, I am using stdiomask to hide the entry of the password entry.
# This will store it into a variable for it to be used when passing this onto 
# the webdriver object.
# Note: Using stdiomask does not encrypt your password, it only masks the entry. 
# Do not consider stdiomask as a completely secure transport protocol. It's only 
# a masking tool. 

password = stdiomask.getpass("Enter Password: ")

# Build the webdriver object. Use it to instantiate the use of the Firefox browser.
# Note: You can utilize other browser drivers, do a search on webdriver options.

driver = webdriver.Firefox()
driver.get("http://gmail.google.com")

# Time to send the credentials over to the driver object. 
driver.find_element_by_id("identifierId").send_keys(username)
driver.find_element_by_id("identifierNext").click()
time.sleep(5)

# Note: At the time of the testing of this, the password is not passing into the field.
# The userid on the other hand is passing to the user name is updating in the browser.
# I don't feel like traversing the mounds of javascript code on google website, but if anyone
# wants to, and update that script that would be nice.
# I'm just providing this as an example of selenium, and some future reference should I need to 
# do this for a project someday.

driver.find_element_by_name("input[type=password]").send_keys(password)
driver.find_element_by_id("passwordNext").click()
time.sleep(5)
