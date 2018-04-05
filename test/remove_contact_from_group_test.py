import random
from fixture.group import Group
from fixture.contact import Contact
from fixture.orm import ORMFixture


def test_remove_contact_from_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    # Check for available contacts and groups
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Fname", middlename="Mname", lastname="Lname", nickname="Nick",
                                   title="TestTitle", company="TestCompany", address="TestAddress", homephone="1111111",
                                   mobilephone="2222222", workphone="3333333", fax="fax",
                                   email="test@test.test", email2="test2@test.test", email3="test3@test.test",
                                   homepage="homepage",
                                   birth="1980", secondaryaddress="TestAddress2", secondaryphone="4444444"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    # Select random group and check for existing contacts
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_in_group(group)) == 0:
        contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_to_group(contact.id, group.name)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    # Select random contact in group and remove it
    contact_to_remove = random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_group(contact_to_remove.id, group.name)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    # Asserts
    assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group)
    old_contacts_in_group.remove(contact_to_remove)
    assert old_contacts_in_group == new_contacts_in_group
    print("\n", "Contact", contact_to_remove.firstname, "was successfully removed from group", group.name)

