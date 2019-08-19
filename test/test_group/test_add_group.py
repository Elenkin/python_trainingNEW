# -*- coding: utf-8 -*-
from model.group import Group
import pytest
#для случайного выбора
import random
#содержит константы хранящие списков символов
import string

#генерация случайных тестовых данных
def random_string(prefix, maxlen):
    #символы которые будем использовать в случайно сгенерированной строке
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    #random.choice - выбирает symbols из заданной строки
    #будет сгенерирована случайная длина НЕ превышающая max
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#выносим тестовые данные из функции
testdata = [
        Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
        #for i in range(5)
]

#добавили передачу тестовых данных в качестве параметра, где group- параметр, testdata - источник, ids - параметр с текстовым представлением
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    #group = Group(name="group_name", header="header", footer="footer")
    app.group.create(group)
    #сравнимаем не со значением длины нового списка а со значениеv rjnjhsq djpdhfoftn метод count
    assert len(old_groups) + 1 == app.group.count_group()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_add_emty_group(app):
    #old_groups = app.group.get_group_list()
   #group = Group(name="", header="", footer="")
    #app.group.create(group)
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) + 1 == len(new_groups)
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


