# import the libraries that we will use

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import tkinter as tk
from tkinter import simpledialog

# function that prompts the user for the url, username and password of the user
def userDetails():
  
    master = tk.Tk()
    tk.Label(master,
             text="Url").grid(row=0,
                              padx=20,
                              pady=5)
    tk.Label(master,
             text="Username").grid(row=1,
                                   padx=20,
                                   pady=5)
    tk.Label(master,
             text="Password").grid(row=2,
                                   padx=20,
                                   pady=5)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    values =[]

    def cont():

        url = e1.get()
        username = e2.get()
        password = e3.get()

        master.destroy()

        values.append(url)
        values.append(username)
        values.append(password)

    tk.Button(master,
              text='Ok', command=cont).grid(row=3,
                                            column=0,
                                            sticky=tk.W,
                                            pady=5,
                                            padx=20)
    tk.Button(master,
              text='Cancel', command=master.quit).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=5,
                                                       padx=20)

    tk.mainloop()

    return values

# call the function to input user details
url, username, password = userDetails()

# get an instance of browser
# executable path is the path to the geckodriver.exe
browser = webdriver.Firefox()
browser.get(url)

# first sign in else we won't be able to get all comments
signin = browser.find_element_by_link_text("Sign in")
signin.click()

# wait for some time before throwing exception
wait = WebDriverWait(browser, 5)

# get fields to enter email id and password
usernamefield = browser.find_element_by_id("username")
passwordfield = browser.find_element_by_id("password")

# find the submit button using css_selector
submit = browser.find_elements_by_css_selector(
    "html.artdeco body.system-fonts div#app__container main.app__content div form.login__form div.login__form_action_container button.btn__primary--large.from__button--floating")

# enter your email id and password
usernamefield.send_keys(username)
passwordfield.send_keys(password)

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
df = pd.DataFrame({'Email id': emails})
df.to_csv('emails.csv', index=False, encoding='utf-8')

# print for terminal
print("--------------------------DONE!!!!!--------------------------")
