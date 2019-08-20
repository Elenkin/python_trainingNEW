from model.contact import Contact
import random
import string
import os.path
import jsonpickle

def random_string(prefix, maxlen):
    symbols = string.ascii_lowercase + string.ascii_uppercase + "-"
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(prefix, maxlen):
    symbols = string.digits + "+" + ")" + "(" + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=random_string("First", 10),
            middlename=random_string("Middl", 10),
            lastname=random_string("last", 10),
            nickname=random_string("Nick",5),
            company=random_string("company", 5),
            address=random_string("address", 5),
            home=random_number("8", 11), mobile=random_number("+7", 12), work=random_number("7", 12),
            email="test@mail.ru", email3="5555@mail.ru", email2="",
            bday="1", bmonth="January", byear="1990")
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contact_with_jsonpickle.json")

with open(file, "w") as f:
    frozen = jsonpickle.encode(testdata)
    f.write(frozen)
