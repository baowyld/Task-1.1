from model.contact import Contact
from random import randrange


def test_modify_some_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="test_firstname", lastname="test_lastname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New_Firstname")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_lastname(app):
#     if app.contact.count_contacts() == 0:
#         app.contact.create(Contact(firstname="test_firstname", lastname="test_lastname"))
#     app.contact.modify_first_contact(Contact(lastname="New_Lastname"))

