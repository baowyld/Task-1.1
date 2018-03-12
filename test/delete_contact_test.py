from model.contact import Contact
from random import randrange


def test_some_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="Fname", middlename="Mname", lastname="Lname", nickname="Nick",
                               title="TestTitle", company="TestCompany", address="TestAddress", homephone="1111111",
                               mobilephone="2222222", workphone="3333333", fax="fax", email="test@test.test", birth="1980",
                               secondaryaddress="TestAddress2", secondaryphone="4444444"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
