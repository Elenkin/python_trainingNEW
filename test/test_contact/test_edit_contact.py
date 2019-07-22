from model.contact import Contact

def test_edit_contact(app):
    app.contact.edit(Contact(firstname="Edit", middlename="Ivanovich", lastname="Ivanov", nickname="Rog",
                                         company="OOO", address="Moscow", mobile="+79260003333", email="123@mail.ru",
                                         bday="1", bmonth="January", byear="1990"))
