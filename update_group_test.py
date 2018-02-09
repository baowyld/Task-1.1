from model.group import Group


def test_update_first_group(app):
    app.session.login(user="admin", password="secret")
    app.helper.update_first_group(Group(name="new_group_name", header="new_group_header", footer="new_group_footer"))
    app.session.logout()

