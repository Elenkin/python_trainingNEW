from model.contact import Contact
from random import randrange

def test_modify_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact(Contact(firstname="YYYYYYY", middlename="ДДДДДД", lastname="YYYYYY", nickname="Rog",
                      company="OOO", address="Moscow",
                      home="+84951112233", mobile="", work="3(333)33333",
                      email="123@mail.ru", email3="5555@mail.ru", email2="",
                      bday="1", bmonth="January", byear="1990"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="YYYYYYY", middlename="ДДДДДД", lastname="YYYYYY", nickname="Rog",
                      company="OOO", address="Moscow",
                      home="+84951112233", mobile="", work="3(333)33333",
                      email="123@mail.ru", email3="5555@mail.ru", email2="",
                      bday="1", bmonth="January", byear="1990")
    #запомнили id
    contact.id = old_contacts[0].id
    app.contact.details_modify(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_by_index(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact(Contact(firstname="YYYYYYY", middlename="ДДДДДД", lastname="YYYYYY", nickname="Rog",
                      company="OOO", address="Moscow",
                      home="+84951112233", mobile="", work="3(333)33333",
                      email="123@mail.ru", email3="5555@mail.ru", email2="",
                      bday="1", bmonth="January", byear="1990"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="YYYYYYY", middlename="ДДДДДД", lastname="YYYYYY", nickname="Rog",
                      company="OOO", address="Moscow",
                      home="+84951112233", mobile="", work="3(333)33333",
                      email="123@mail.ru", email3="5555@mail.ru", email2="",
                      bday="1", bmonth="January", byear="1990")
    #запомнили id
    contact.id = old_contacts[index].id
    app.contact.details_modify_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
