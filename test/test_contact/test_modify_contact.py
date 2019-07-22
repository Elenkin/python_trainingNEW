from model.contact import Contact

def test_modify_contact(app):
    app.contact.details_modify(Contact(firstname="Modify", middlename="Ivanovich", lastname="Ivanov", nickname="Rog",
                                         company="OOO", address="Moscow", mobile="+79260002222", email="123@mail.ru",
                                         bday="1", bmonth="January", byear="1990"))
