### python program to create a student class with constructor having more than
## one parameter

class Student:
    ''' '''
    # this is a constructor
    def __init__(self, n = ' ', m = 0):
         self.name = n
         self.marks = m

    # this is an instance method
    def display(self):
         print('Hi ', self.name)
         print('Your marks: ', self.marks)


# constructor called without any arguments

s = Student(n='Anurag', m=100)
s.display()
print('----------')

def check_input(marks):
    if marks == '':
        marks = 0
    return marks

## constructor is called with 2 arguments
name = input('Enter your name: ')
marks = check_input(input('Enter your marks: '))


s1 = Student(name, marks)
## s1 = Student('Anurag', 900)
s1.display()
print('----------')
