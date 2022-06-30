## formatting the string

fname = input('Enter you first name: ')
mname = input('Enter you middle name: ')
lname = input('Enter you last name: ')

print("My name is {}".format(fname))
print("This is my fullname {} {} {}".format(fname, mname, lname))
print(f"This is my fullname {fname} {mname} {lname}")
