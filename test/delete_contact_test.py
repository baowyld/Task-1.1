
def test_delete_first_contact(app):
    app.session.login(user="admin", password="secret")
    app.helper.delete_first_contact()
    app.session.logout()
