# import the libraries that we will use

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


# url of the post that you want to scrape
url = "https://www.linkedin.com/posts/nikhilnaren_table-of-contents-activity-6662754592826232832-OFHm/"

# get an instance of browser
browser = webdriver.Firefox()
browser.get(url)

# first sign in else we won't be able to get all comments
signin = browser.find_element_by_link_text("Sign in")
signin.click()

# wait for some time before throwing exception
wait = WebDriverWait( browser, 5 )

# get fields to enter email id and password
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

# find the submit button using css_selector
submit   = browser.find_elements_by_css_selector("html.artdeco body.system-fonts div#app__container main.app__content div form.login__form div.login__form_action_container button.btn__primary--large.from__button--floating")

# enter your email id and password
username.send_keys("youremail@gmail.com")
password.send_keys("yourpassword")

# click on submit
submit[0].click()
WebDriverWait(browser, 5)


# get all objects from comment section
email_objects = browser.find_elements_by_xpath("//a[@class='feed-link ember-view']")

# make a list to store extracted emails
emails = []
for e in email_objects:
    emails.append(e.text)    

# create .csv file and copy all data to it.
df = pd.DataFrame({'Email id':emails})
df.to_csv('emails.csv',index = False, encoding='utf-8')

# print for terminal
print("--------------------------DONE!!!!!--------------------------")

#----------------------------------------------------------------Completed----------------------------------------------------------------



