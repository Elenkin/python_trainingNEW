from sys import maxsize

class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    #как выглядит строковое представление Объекта выведенного в консоли
    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)

    #сравнение объектов по смыслу (поэлементное сравнение двух списков)
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize