
def test_delete_first_group(app):
    app.session.login(user="admin", password="secret")
    app.helper.delete_first_group()
    app.session.logout()

