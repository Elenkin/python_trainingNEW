# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.add_contact import testdata

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new(app, contact):
    old_contacts = app.contact.get_contact_list()
    #локальная переменная которая создает Контакт
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#обращаемся в каталог data к файлу json с именем contacts
def test_add_new_json(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    #локальная переменная которая создает Контакт
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_new_json_check_db(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_new_contact(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


