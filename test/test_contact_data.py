import re
from random import randrange
from model.contact import Contact


def test_all_contacts_data(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Fname", middlename="Mname", lastname="Lname", nickname="Nick",
                      title="TestTitle", company="TestCompany", address="TestAddress", homephone="1111111",
                      mobilephone="2222222", workphone="3333333", fax="fax",
                      email="test@test.test", email2="test2@test.test", email3="test3@test.test", homepage="homepage",
                      birth="1980", secondaryaddress="TestAddress2", secondaryphone="4444444"))
    contacts_hp = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_hp) == len(contacts_db)
    for i in range(len(contacts_db)):
        assert contacts_hp[i].lastname == contacts_db[i].lastname
        assert contacts_hp[i].firstname == contacts_db[i].firstname
        assert contacts_hp[i].address == contacts_db[i].address
        print("On home page: ", "\n", contacts_hp[i])
        print("In database: ", "\n", contacts_db[i], "\n", "----------------------------------------------------")


def test_random_contact_data(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))
