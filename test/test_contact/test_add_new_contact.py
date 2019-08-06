# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new(app):
    old_contacts = app.contact.get_contact_list()
    #локальная переменная которая создает Контакт
    contact = Contact(firstname="name", middlename="Ivanovich", lastname="Petrov", nickname="Rog",
                                         company="OOO", address="Moscow", mobile="+79260001111", email="123@mail.ru",
                                         bday="1", bmonth="January", byear="1990")
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


