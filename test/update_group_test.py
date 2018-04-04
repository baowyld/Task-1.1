from model.group import Group
import random


def test_modify_some_group_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    updated_group = Group(name="New group name", id=group.id)
    app.group.modify_group_by_id(group.id, updated_group)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(updated_group)
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
