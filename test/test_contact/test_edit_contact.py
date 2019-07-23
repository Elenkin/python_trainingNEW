from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Rog",
                                         company="OOO", address="Moscow", mobile="+79260003333", email="123@mail.ru",
                                         bday="1", bmonth="January", byear="1990"))
    app.contact.edit(Contact(firstname="Edit", middlename="Ivanovich", lastname="Ivanov", nickname="Rog",
                                         company="OOO", address="Moscow", mobile="+79260003333", email="123@mail.ru",
                                         bday="1", bmonth="January", byear="1990"))
