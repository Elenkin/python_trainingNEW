from model.group import Group

def test_delete_first_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    app.group.delete_first_group()
