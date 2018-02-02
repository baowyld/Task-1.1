# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import ContactApplication


@pytest.fixture
def app(request):
    fixture = ContactApplication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact_test(app):
    app.session.login(user="admin", password="secret")
    app.create_new_contact(Contact(firstname="Fname", middlename="Mname", lastname="Lname", company="TestCompany", address="TestAddress", homephone="111-11-11", mobilephone="222-22-22",
                                workphone="333-33-33", email="test@test.test", birth="1980", secondaryaddress="TestHomeAddress", secondaryhomenumber="444-44-44"))
    app.session.logout()


