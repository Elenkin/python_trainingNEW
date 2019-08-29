import re
from random import randrange
from fixture.contact import Contact

def test_phones_on_homepage(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)
    assert contact_from_home_page.firstname == clear(contact_from_edit_page.firstname)
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)

# def test_phones_on_view_homepage(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.home == contact_from_edit_page.home
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#     assert contact_from_view_page.work == contact_from_edit_page.work

#сравнение списка контактов с главной страницы со списком из ДБ
def test_phones_on_homepage_check_db(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert len(contact_from_home_page) == len(contact_from_db)
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.home, contact.mobile, contact.work]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3]))))






