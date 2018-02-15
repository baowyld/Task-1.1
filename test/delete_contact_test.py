from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="test_firstname", lastname="test_lastname"))
    app.contact.delete_first()
