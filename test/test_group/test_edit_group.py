from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="NEW_group", header="header", footer="footer"))
    app.session.logout()

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="NEW_group"))
    app.session.logout()