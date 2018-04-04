import pymysql.cursors
from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            #cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            cursor.execute("select id, firstname, middlename, lastname, nickname, title, company, address, home, mobile,"
                           " work, fax, email, email2, email3, homepage, address2, phone2 from addressbook"
                           " where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                # (id, firstname, lastname) = row
                # list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
                (id, firstname, middlename, lastname, nickname, title, company, address, homephone, mobilephone,
                 workphone, fax, email, email2, email3, homepage, secondaryaddress, secondaryphone) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                    nickname=nickname, title=title, company=company, address=address,
                                    homephone=homephone, mobilephone=mobilephone, workphone=workphone, fax=fax,
                                    email=email, email2=email2, email3=email3, homepage=homepage,
                                    secondaryaddress=secondaryaddress, secondaryphone=secondaryphone))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
