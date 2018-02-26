from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Fname", middlename="Mname", lastname="Lname", nickname="Nick",
                               title="TestTitle", company="TestCompany", address="TestAddress", homephone="111-11-11",
                               mobilephone="222-22-22", workphone="333-33-33", email="test@test.test", birth="1980",
                               secondaryaddress="TestHomeAddress", secondaryhomenumber="444-44-44")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


