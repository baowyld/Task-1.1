from model.contact import Contact
import random


def test_modify_some_contact_firstname(app, db, check_ui):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="Fname", middlename="Mname", lastname="Lname", nickname="Nick",
                      title="TestTitle", company="TestCompany", address="TestAddress", homephone="1111111",
                      mobilephone="2222222", workphone="3333333", fax="fax",
                      email="test@test.test", email2="test2@test.test", email3="test3@test.test", homepage="homepage",
                      birth="1980", secondaryaddress="TestAddress2", secondaryphone="4444444"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    updated_contact = Contact(firstname="New_Firstname", id=contact.id)
    app.contact.modify_contact_by_id(contact.id, updated_contact)
    app.open_home_page()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(updated_contact)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



