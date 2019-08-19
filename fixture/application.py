from selenium import webdriver
from fixture.session import sessionHelper
from fixture.group import groupHelper
from fixture.contact import contactHelper

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome('C:\\Users\\e.pavlova\\Desktop\\tmp\\chromedriver_win32\\chromedriver.exe')
            #self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd == webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        #self.wd.implicitly_wait(5)
        self.session = sessionHelper(self)
        self.group = groupHelper(self)
        self.contact = contactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        #wd.get("http://localhost:8080/addressbook/")
        wd.get(self.base_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()


