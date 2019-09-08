from model.group import Group
from model.contact import Contact
import random


def test_add_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(Contact(firstname="YYYYYYY", middlename="ДДДДДД", lastname="YYYYYY", nickname="Rog",
                      company="OOO", address="Moscow",
                      home="+84951112233", mobile="", work="3(333)33333",
                      email="123@mail.ru", email3="5555@mail.ru", email2="",
                      bday="1", bmonth="January", byear="1990"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    old_contacts_in_group = db.get_contact_list_from_group()
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_in_group(contact.id, group.name)
    new_contacts_in_group = db.get_contact_list_from_group()
    print(len(old_contacts_in_group))
    print(len(new_contacts_in_group))
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)



