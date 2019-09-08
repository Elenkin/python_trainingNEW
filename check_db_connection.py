# import pymysql.cursors
from model.group import Group
#
# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()


from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()


# from fixture.orm import ORMFixture
#
# db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# try:
#     list = db.get_contact_list()
#     for item in list:
#         print(item)
#     print(len(list))
# finally:
#     pass

#
# from fixture.orm import ORMFixture
#
# db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# try:
#     #id table address_in_groups column group_id
#     list = db.get_contacts_not_in_group(Group(id=226))
#     for item in list:
#         print(item)
#     print(len(list))
# finally:
#     pass