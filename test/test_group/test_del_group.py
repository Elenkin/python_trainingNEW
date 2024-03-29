from model.group import Group
import random
from random import randrange

# def test_delete_first_group(app):
#     if app.group.count_group() == 0:
#         app.group.create(Group(name="test", header="header", footer="footer"))
#     old_groups = app.group.get_group_list()
#     #выбираем случайный индекс
#     index = randrange(len(old_groups))
#     app.group.delete_group_by_index(index)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) - 1 == len(new_groups)
#     #удаление 1 элемента списка
#     old_groups[index:index+1] = []
#     assert old_groups == new_groups
#
# def test_delete_group(app, db, check_ui):
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="test", header="header", footer="footer"))
#     old_groups = db.get_group_list()
#     group = random.choice(old_groups)
#     app.group.delete_group_by_id(group.id)
#     new_groups = db.get_group_list()
#     assert len(old_groups) - 1 == len(new_groups)
#     #удаление 1 элемента списка
#     old_groups.remove(group)
#     assert old_groups == new_groups
#     if check_ui:
#         assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def test_delete_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    #удаление 1 элемента списка
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
