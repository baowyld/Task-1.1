from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.app.open_home_page()
        self.open_new_contact_page()
        wd = self.app.wd
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

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
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("byear", contact.birth)
        self.change_field_value("address2", contact.secondaryaddress)
        self.change_field_value("phone2", contact.secondaryphone)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath(".//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_first(self):
        self.delete_contact_by_index(0)

    def open_new_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_contact_updater_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath(".//img[@title='Edit']")[index].click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        # self.select_contact_by_index(index)
        # self.open_contact_updater_by_index(index)
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_modified_contact_by_id(id)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def select_modified_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def count_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                    cells = element.find_elements_by_tag_name("td")
                    lastname = cells[1].text
                    firstname = cells[2].text
                    address = cells[3].text
                    id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                    all_emails = cells[4].text
                    all_phones = cells[5].text
                    self.contact_cache.append(Contact(firstname=firstname, lastname=lastname,
                                                      id=id, address=address, all_emails_from_home_page=all_emails,
                                                      all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").text
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def add_contact_to_group(self, id, name):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        self.choose_group_by_name(name)
        wd.find_element_by_name("add").click()

    def choose_group_by_name(self, name):
        wd = self.app.wd
        Select(wd.find_element_by_xpath(".//select[@name='to_group']")).select_by_visible_text(name)

    def delete_contact_from_group(self, id, name):
        wd = self.app.wd
        self.app.open_home_page()
        self.choose_group_on_contacts_page(name)
        self.select_contact_by_id(id)
        wd.find_element_by_name("remove").click()

    def choose_group_on_contacts_page(self, name):
        wd = self.app.wd
        Select(wd.find_element_by_xpath(".//select[@name='group']")).select_by_visible_text(name)