from model.contact import Contact

def test_contact_details(app):
    app.session.login(username="admin", password="secret")
    app.contact.details_modify(Contact(firstname="NEW", middlename="Ivanovich", lastname="Ivanov", nickname="Rog",
                                         company="OOO", address="Moscow", mobile="+79260001111", email="123@mail.ru",
                                         bday="1", bmonth="January", byear="1990"))
    app.session.logout()