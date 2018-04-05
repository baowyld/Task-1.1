import random
from fixture.group import Group
from fixture.contact import Contact
from fixture.orm import ORMFixture


def test_add_contact_to_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    # Check for available contacts and groups
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Fname", middlename="Mname", lastname="Lname", nickname="Nick",
                      title="TestTitle", company="TestCompany", address="TestAddress", homephone="1111111",
                      mobilephone="2222222", workphone="3333333", fax="fax",
                      email="test@test.test", email2="test2@test.test", email3="test3@test.test", homepage="homepage",
                      birth="1980", secondaryaddress="TestAddress2", secondaryphone="4444444"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    # Selection of random group and contact
    app.open_home_page()
    contact = random.choice(orm.get_contact_list())
    group = random.choice(orm.get_group_list())
    old_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    # Adding of contact to group
    app.contact.add_contact_to_group(contact.id, group.name)
    new_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    if len(old_contacts_in_group) == len(new_contacts_in_group):
        print("\n", "Same group was chosen for the selected contact, please retry")
    else:
        assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
        for contact_in_group in new_contacts_in_group:
            assert (contact_in_group.id == contact.id)
            print("\n", "Contact ", contact.firstname, "was successfully added to group ", group.name)
