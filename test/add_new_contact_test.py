from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Fname", middlename="Mname", lastname="Lname", nickname="Nick",
                               title="TestTitle", company="TestCompany", address="TestAddress", homephone="1111111",
                               mobilephone="2222222", workphone="3333333", fax="fax", email="test@test.test", birth="1980",
                               secondaryaddress="TestAddress2", secondaryphone="4444444")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



