# Switch on your WiFi and connect to VIT 2.4G or VIT 5G
# then run this script
# This script will give the user two options:
# 1) Login (if the user is not logged in to the VIT WiFi)
# 2) Logout (if the user is already logged in to the VIT WiFi)

from selenium import webdriver
import getpass                   # For taking user input for password as hidden
import os

# URLs for login and logout
login_url = "http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://go.microsoft.com/fwlink/&LinkID=219472&clcid=0x409"
logout_url = "http://phc.prontonetworks.com/cgi-bin/authlogout"

# Thats the chromedriver which will handle the chrome browser and handle the whole operation automatically yet visible on the browser (slower than phantom js)
chromedriver = "chromedriver.exe"

#Thats the phantom js driver which will handle the whole browser action seemlessly fast and hidden 
phantomjs = "phantomjs.exe"

print("What do you wanna do?")
print("\n1) Login to VIT WiFi")
print("2)Logout from VIT WiFi\n")
choice = ""

while (choice != "1" and choice!="2"):
    choice = input()
    if (choice == "1"):
        # Taking user input
        regnum = input("Enter your Registration number:\n")
        passwordtext = getpass.getpass("Enter your password:\n")

        os.system('cls')

        print("What do you wanna do?")
        print("\n1) Watch the whole log in thing perform automatically on a Chrome browser, like Magic!!! ???")
        print("2) Make the whole log in thing run in background(Quite boring but super FAST!!!!!) ???\n")
        choice2 = int(input())

        if (choice != 1 or choice != 2):
            print("You entered wrong choice")
            continue
        elif (choice == 1):
            browser = webdriver.Chrome(chromedriver)
        else:
            browser = webdriver.PhantomJS(phantomjs)

        browser.get(login_url)

        # Finding the fields in the form
        username = browser.find_element_by_name("userId")
        password = browser.find_element_by_name("password")

        # Sending the user data on the form
        username.send_keys(regnum)
        password.send_keys(passwordtext)

        # Handling the click event of the login button
        browser.find_element_by_name("Submit22").click()
        browser.close()
        browser.quit()

    elif (choice == "2"):
        browser = webdriver.PhantomJS(phantomjs)
        browser.get(logout_url)
        browser.close()
        browser.quit()
    else:
        print("Please enter correct choice\n")