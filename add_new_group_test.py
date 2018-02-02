# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import GroupApplication


@pytest.fixture()
def app(request):
    fixture = GroupApplication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.login(user="admin", password="secret")
    app.create_group(Group(name="g1name", header="g1header", footer="g1footer"))
    app.logout()


def test_add_new_empty_group(app):
    app.login(user="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

