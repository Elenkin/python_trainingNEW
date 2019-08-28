
from model.contact import Contact
from random import randrange
import random

def test_del_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact(Contact(firstname="YYYYYYY", middlename="ДДДДДД", lastname="YYYYYY", nickname="Rog",
                      company="OOO", address="Moscow",
                      home="+84951112233", mobile="", work="3(333)33333",
                      email="123@mail.ru", email3="5555@mail.ru", email2="",
                      bday="1", bmonth="January", byear="1990"))
    old_contacts = app.contact.get_contact_list()
    app.contact.del_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

def test_del_contact_by_index(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact(Contact(firstname="YYYYYYY", middlename="ДДДДДД", lastname="YYYYYY", nickname="Rog",
                      company="OOO", address="Moscow",
                      home="+84951112233", mobile="", work="3(333)33333",
                      email="123@mail.ru", email3="5555@mail.ru", email2="",
                      bday="1", bmonth="January", byear="1990"))
    old_contacts = app.contact.get_contact_list()
    # выбираем случайный индекс
    index = randrange(len(old_contacts))
    app.contact.del_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

def test_del_contact_check_db(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(Contact(firstname="YYYYYYY", middlename="ДДДДДД", lastname="YYYYYY", nickname="Rog",
                      company="OOO", address="Moscow",
                      home="+84951112233", mobile="", work="3(333)33333",
                      email="123@mail.ru", email3="5555@mail.ru", email2="",
                      bday="1", bmonth="January", byear="1990"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.del_contact_by_id(contact.id)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    #удаляем контакт из БД
    old_contacts.remove(contact)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


