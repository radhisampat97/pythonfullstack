# understanding class creation

class Student:
    '''This is the static class of student'''

    #The below block defines the attributes of student
    def __init__(self):
         self.name = 'Radhika'
         self.age = 25
         self.marks = 900

    # the below block defines a method
    def talk(self):
         print('Hi, I am ', self.name)
         print('My age is ', self.name)
         print('My marks are ', self.name)

a = Student()
abc = Student()
a.talk()

# memory location assigned to Student object
print(id(a))
print()

# memory location assigned to a.talk() object
print('Id of a.talk(): ', id(a.talk))

##
# to print the variables and it memory location
print(a.name)
print(id(a.name))
print()

print(a.age)
print(id(a.age))
print()

print(a.marks)
print(id(a.marks))
##
#

