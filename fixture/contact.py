class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.app.open_home_page()
        self.open_new_contact_menu()
        # init_contact creation
        wd = self.app.wd
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("byear", contact.birth)
        self.change_field_value("address2", contact.secondaryaddress)
        self.change_field_value("phone2", contact.secondaryhomenumber)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    # def modify_first_contact(self, contact):
    #     wd = self.app.wd
    #     self.app.open_home_page()
    #     self.select_first_contact()
    #     self.open_contact_updater()
    #     # update contact details
    #     wd.find_element_by_name("firstname").click()
    #     wd.find_element_by_name("firstname").clear()
    #     wd.find_element_by_name("firstname").send_keys(contact.firstname)
    #     wd.find_element_by_name("middlename").click()
    #     wd.find_element_by_name("middlename").clear()
    #     wd.find_element_by_name("middlename").send_keys(contact.middlename)
    #     wd.find_element_by_name("lastname").click()
    #     wd.find_element_by_name("lastname").clear()
    #     wd.find_element_by_name("lastname").send_keys(contact.lastname)
    #     wd.find_element_by_name("nickname").click()
    #     wd.find_element_by_name("title").click()
    #     wd.find_element_by_name("company").click()
    #     wd.find_element_by_name("company").clear()
    #     wd.find_element_by_name("company").send_keys(contact.company)
    #     wd.find_element_by_name("address").click()
    #     wd.find_element_by_name("address").clear()
    #     wd.find_element_by_name("address").send_keys(contact.address)
    #     wd.find_element_by_name("home").click()
    #     wd.find_element_by_name("home").clear()
    #     wd.find_element_by_name("home").send_keys(contact.homephone)
    #     wd.find_element_by_name("mobile").click()
    #     wd.find_element_by_name("mobile").clear()
    #     wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
    #     wd.find_element_by_name("work").click()
    #     wd.find_element_by_name("work").clear()
    #     wd.find_element_by_name("work").send_keys(contact.workphone)
    #     wd.find_element_by_name("email").click()
    #     wd.find_element_by_name("email").clear()
    #     wd.find_element_by_name("email").send_keys(contact.email)
    #     wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
    #     wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
    #     wd.find_element_by_name("byear").click()
    #     wd.find_element_by_name("byear").clear()
    #     wd.find_element_by_name("byear").send_keys(contact.birth)
    #     wd.find_element_by_name("address2").click()
    #     wd.find_element_by_name("address2").clear()
    #     wd.find_element_by_name("address2").send_keys(contact.secondaryaddress)
    #     wd.find_element_by_name("phone2").click()
    #     wd.find_element_by_name("phone2").clear()
    #     wd.find_element_by_name("phone2").send_keys(contact.secondaryhomenumber)
    #     # submit update
    #     wd.find_element_by_name("update").click()

    def open_new_contact_menu(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_contact_updater(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        self.open_contact_updater()
        # fill the form
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()