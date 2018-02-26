from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="test_firstname", lastname="test_lastname"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New_Firstname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_lastname(app):
#     if app.contact.count_contacts() == 0:
#         app.contact.create(Contact(firstname="test_firstname", lastname="test_lastname"))
#     app.contact.modify_first_contact(Contact(lastname="New_Lastname"))

