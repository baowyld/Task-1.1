from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="test_firstname", lastname="test_lastname"))
    app.contact.modify_first_contact(Contact(firstname="New_Firstname"))


def test_modify_contact_lastname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="test_firstname", lastname="test_lastname"))
    app.contact.modify_first_contact(Contact(lastname="New_Lastname"))

