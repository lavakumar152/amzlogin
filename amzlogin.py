from selenium import webdriver
from getpass import getpass

username = input('Enter your user name: ')
password = getpass('Enter your password : ')

driver = webdriver.Chrome('E:\\Udemy\\python\\webdriver\\chromedriver.exe')
driver.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

username_textbox = driver.find_element_by_id('ap_email')
username_textbox.send_keys(username)

continue_button = driver.find_element_by_id('continue')
continue_button.submit()

password_textbox = driver.find_element_by_id('ap_password')
password_textbox.send_keys(password)

login_button = driver.find_element_by_id('signInSubmit')
login_button.submit()
