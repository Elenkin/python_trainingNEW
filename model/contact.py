
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None, mobile=None, email=None, bday=None, bmonth=None, byear=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.mobile = mobile
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id

    def __repr__(self):
        return "%s: %s %s" % (self.id, self.lastname, self.firstname)

    #def __eq__(self, other):
        #return self.id == other.id and self.lastname == other.lastname and self.firstname == other.firstname


