from model.group import Group
from random import randrange

def test_edit_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    #выбираем случайный индекс
    index = randrange(len(old_groups))
    group = Group(name="NEW_group", header="header", footer="footer")
    #запомнили id группы
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_edit_first_group(app):
#    if app.group.count_group() == 0:
#       app.group.create(Group(name="test", header="header", footer="footer"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name="Modify_name"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
