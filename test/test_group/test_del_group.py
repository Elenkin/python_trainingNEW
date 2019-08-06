from model.group import Group
from random import randrange

def test_delete_first_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    #выбираем случайный индекс
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    #удаление 1 элемента списка
    old_groups[index:index+1] = []
    assert old_groups == new_groups
