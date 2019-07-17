
from model.contact import Contact

def test_del_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_all_contact()
    app.session.logout()


def test_add_new(app):
    app.session.login( username="admin", password="secret")
    app.contact.add_new_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Rog",
                                         company="OOO", address="Moscow", mobile="+79260001111", email="123@mail.ru",
                                         bday="1", bmonth="January", byear="1990"))
    app.session.logout()
