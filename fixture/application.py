from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import GroupSessionHelper, ContactSessionHelper
from fixture.helper import GroupHelper, ContactHelper


class GroupApplication:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = GroupSessionHelper(self)
        self.helper = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()


class ContactApplication:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = ContactSessionHelper(self)
        self.helper = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

