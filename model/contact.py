from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None,
                 home=None, mobile=None, work=None,
                 email=None, email3=None, email2=None,
                 bday=None, bmonth=None, byear=None, id=None, all_phones_from_home_page=None, all_email_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.email = email
        self.email3 = email3
        self.email2 = email2
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s: %s %s %s %s" % (self.id, self.lastname, self.firstname, self.email, self.home)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize




