from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="Fname", middlename="Mname", lastname="Lname", nickname="Nick",
                      title="TestTitle", company="TestCompany", address="TestAddress", homephone="1111111",
                      mobilephone="2222222", workphone="3333333", fax="fax",
                      email="test@test.test", email2="test2@test.test", email3="test3@test.test", homepage="homepage",
                      birth="1980", secondaryaddress="TestAddress2", secondaryphone="4444444"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    app.open_home_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
