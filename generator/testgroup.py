from model.group import Group
import random
import string
import os.path
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of group", "file"])
except getopt.GetoptError as err:
     getopt.usage()
     sys.exit(2)

n = 5
f = "data\group with jsonpickle.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
        Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
        for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as f:
    frozen = jsonpickle.encode(testdata)
    f.write(frozen)