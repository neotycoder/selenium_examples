# Description: This script performs a google search on the command line.
# It uses the selenium module.
# This is a simple example of how to use the selenium driver
# to perform a Google search. 

# Note: There are other examples on how to use the selenium driver.
# Example: Automate how to perform web testing for an application.
# Example: Send login credentials to automate login to a secure website.

# Requirements:
# pip3 install selenium

from selenium import webdriver 

# Input a string to search, and store it into a variable.

search = input("Search Criteria: ")

# Instantiate a browser object with the Firefox browser.
browser = webdriver.Firefox()

# Append the search critera to your get request in the browser object get method call.
# This will open up a Firefox browser with a listing of your search results.
browser.get("https://www.google.com/search?q=" + search + "&start=")

