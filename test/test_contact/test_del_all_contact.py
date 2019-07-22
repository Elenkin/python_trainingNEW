
from model.contact import Contact

def test_del_all_contact(app):
    app.contact.del_all_contact()
    app.contact.add_new_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Rog",
                                         company="OOO", address="Moscow", mobile="+79260001111", email="123@mail.ru",
                                         bday="1", bmonth="January", byear="1990"))

