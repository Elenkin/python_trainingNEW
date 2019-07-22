from model.group import Group

def test_edit_group(app):
    app.group.edit(Group(name="NEW_group", header="header", footer="footer"))

def test_edit_first_group(app):
    app.group.modify_first_group(Group(name="NEW_group"))
