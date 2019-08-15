# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_lowercase + string.ascii_uppercase + "-"
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(prefix, maxlen):
    symbols = string.digits + "+" + ")" + "(" + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=random_string("First", 10),
            middlename=random_string("Middl", 10),
            lastname=random_string("last", 10),
            nickname=random_string("Nick",5),
            company=random_string("company", 5),
            address=random_string("address", 5),
            home=random_number("8", 11), mobile=random_number("+7", 12), work=random_number("7", 12),
            email="test@mail.ru", email3="5555@mail.ru", email2="",
            bday="1", bmonth="January", byear="1990")
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new(app, contact):
    pass
    old_contacts = app.contact.get_contact_list()
    #локальная переменная которая создает Контакт
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


