from model.group import Group

def test_edit_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    app.group.edit(Group(name="NEW_group", header="header", footer="footer"))

def test_edit_first_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    app.group.modify_first_group(Group(name="Modify_name"))
