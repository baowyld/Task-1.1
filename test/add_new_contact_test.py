from model.contact import Contact


def test_add_new_contact(app):
    app.contact.create(Contact(firstname="Fname", middlename="Mname", lastname="Lname", nickname="Nick",
                               title="TestTitle", company="TestCompany", address="TestAddress", homephone="111-11-11",
                               mobilephone="222-22-22", workphone="333-33-33", email="test@test.test", birth="1980",
                               secondaryaddress="TestHomeAddress", secondaryhomenumber="444-44-44"))


