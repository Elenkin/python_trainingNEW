
from selenium import webdriver
from fixture.session import sessionHelper
from fixture.group import groupHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome('C:\\Users\\e.pavlova\\Desktop\\tmp\\chromedriver_win32\\chromedriver.exe')
        self.wd.implicitly_wait(60)
        self.session = sessionHelper(self)
        self.group = groupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def destroy(self):
        self.wd.quit()


