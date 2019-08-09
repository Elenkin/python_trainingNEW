from model.contact import Contact

def test_del_from_edit_form(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact(Contact(firstname="NEW", middlename="Ivanovich", lastname="Ivanov", nickname="Rog",
                                            company="OOO", address="Moscow",
                                            home="84951112233", mobile="79260001111", work="333333333", email="123@mail.ru",
                                            bday="1", bmonth="January", byear="1990"))
    old_contacts = app.contact.get_contact_list()
    app.contact.del_from_edit_form()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)