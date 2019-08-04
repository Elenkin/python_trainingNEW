# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Rog",
                                         company="OOO", address="Moscow", mobile="+79260001111", email="123@mail.ru",
                                         bday="1", bmonth="January", byear="1990"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


