
from selenium import webdriver
from fixture.session import sessionHelper
from fixture.group import groupHelper
from fixture.contact import contactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome('C:\\Users\\e.pavlova\\Desktop\\tmp\\chromedriver_win32\\chromedriver.exe')
        #self.wd.implicitly_wait(5)
        self.session = sessionHelper(self)
        self.group = groupHelper(self)
        self.contact = contactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def is_valid(self):
        try:
            self.wd.current_url
            return  True
        except:
            return  False

    def destroy(self):
        self.wd.quit()


