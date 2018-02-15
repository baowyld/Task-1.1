# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.group.create(Group(name="g1name", header="g1header", footer="g1footer"))


def test_add_new_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

