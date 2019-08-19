# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.add_contact import testdata

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


