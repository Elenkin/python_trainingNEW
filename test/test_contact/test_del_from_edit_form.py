from model.contact import Contact

def test_del_from_edit_form(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact(Contact(firstname="YYYYYYY", middlename="ДДДДДД", lastname="YYYYYY", nickname="Rog",
                      company="OOO", address="Moscow",
                      home="+84951112233", mobile="", work="3(333)33333",
                      email="123@mail.ru", email3="5555@mail.ru", email2="",
                      bday="1", bmonth="January", byear="1990"))
    old_contacts = app.contact.get_contact_list()
    app.contact.del_from_edit_form()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)