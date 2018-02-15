from model.contact import Contact


def test_update_first_contact_test(app):
    app.contact.update_first(Contact(firstname="upd_Fname", middlename="upd_Mname", lastname="upd_Lname", company="upd_TestCompany", address="upd_TestAddress", homephone="555-55-55", mobilephone="666-66-66",
                                     workphone="777-77-77", email="upd_test@test.test", birth="1990", secondaryaddress="upd_TestHomeAddress", secondaryhomenumber="888-88-88"))
