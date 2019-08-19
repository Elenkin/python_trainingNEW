from model.group import Group
#для случайного выбора
import random
#содержит константы хранящие списков символов
import string


constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]
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
        for i in range(5)
]
