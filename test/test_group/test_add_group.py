# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.groups import testdata


#добавили передачу тестовых данных в качестве параметра, где group- параметр, testdata - источник, ids - параметр с текстовым представлением
#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
# def test_add_group(app, json_groups):
#     group = json_groups
#     old_groups = app.group.get_group_list()
#     app.group.create(group)
#     #сравнимаем не со значением длины нового списка а со значениеv rjnjhsq djpdhfoftn метод count
#     assert len(old_groups) + 1 == app.group.count_group()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    print(len(old_groups), len(new_groups))
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




