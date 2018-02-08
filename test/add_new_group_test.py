# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.session.login(user="admin", password="secret")
    app.helper.create_group(Group(name="g1name", header="g1header", footer="g1footer"))
    app.session.logout()


def test_add_new_empty_group(app):
    app.session.login(user="admin", password="secret")
    app.helper.create_group(Group(name="", header="", footer=""))
    app.session.logout()

