from model.contact import Contact

def test_del_from_modify_form(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact(Contact(firstname="NEW", middlename="Ivanovich", lastname="Ivanov", nickname="Rog",
                                            company="OOO", address="Moscow", mobile="+79260001111", email="123@mail.ru",
                                            bday="1", bmonth="January", byear="1990"))
    app.contact.del_from_modify_form()

