# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import GroupApplication


@pytest.fixture()
def app(request):
    fixture = GroupApplication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.session.login(user="admin", password="secret")
    app.helper.create(Group(name="g1name", header="g1header", footer="g1footer"))
    app.session.logout()


def test_add_new_empty_group(app):
    app.session.login(user="admin", password="secret")
    app.helper.create(Group(name="", header="", footer=""))
    app.session.logout()

