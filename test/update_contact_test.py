from model.contact import Contact
from random import randrange


def test_modify_some_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="Fname", middlename="Mname", lastname="Lname", nickname="Nick",
                      title="TestTitle", company="TestCompany", address="TestAddress", homephone="1111111",
                      mobilephone="2222222", workphone="3333333", fax="fax",
                      email="test@test.test", email2="test2@test.test", email3="test3@test.test", homepage="homepage",
                      birth="1980", secondaryaddress="TestAddress2", secondaryphone="4444444"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New_Firstname")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



