
def test_contact_details(app):
    app.session.login(username="admin", password="secret")
    app.contact.details_modify()
    app.session.logout()