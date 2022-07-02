# Types of methods

# 1 Instance method
#   a Accessor method
#   b Mutator method
# 2 Class method
# 3 Static method

# instance method to process data of the objects

class Student:
     ''' '''
     # this is a constructor
     def __init__(self, n = ' ', m = 0):
          self.name = n    # instance variable
          self.marks = m   # instance variable

     # this is an instance method, and accessor method
     def display(self):
          print('Hi my name is: ', self.name)
          print('My marks are: ', self.marks)

     # to calculate grades based on marks is also an instance method
     # this is a mutator method
     def calculate(self):
          if (self.marks>=600):
               print('You got first grade')
          elif(self.marks>=500):
               print('You got second grade')
          elif(self.marks>=350):
               print('You got third grade')
          else:
               print('Better luck next time!')


##
# create instance with some data from keyword
## n = int(input('How many students?'))
##
##i=10
##while(i<n):

name = input('Enter name: ')
marks = int(input('Enter marks: '))

# create student class instance and store data
s = Student(name, marks)
s.display()
s.calculate()
##i += 1
print('------'*10)


## python program to use class method to handle common feature of all instance

## understanding class method

class Bird:
     ''' '''
     # this is a class var
     wings = 2

     # this is a class method
     @classmethod
     def fly(cls,name):
          print(f'{name} flies with {Bird.wings} wings')
##          print('{} flies with {} wings'.format(name,ArithmeticError cls.wings)

# display information of 2 birds
Bird.fly('Sparrow')
Bird.fly('Pigeon')

##
##python program to create a static method that counts the number of instances
##
# understanding static method

class Myclass:
     ''' '''
     # this is class var or static var
     n = 0

     # constructor that increments n when an instance is created
     def __init__(self):
          Myclass.n = Myclass.n+1         # a = a+1
          
##  def variable_class(cls):
#             print(cls.n)

     # This is a static method to display the no.of instances
     @staticmethod
     def noObjects():
          print(f'No. of instances created: {Myclass.n}')

# create 3 instances
obj1 = Myclass()
Myclass.noObjects()

obj2 = Myclass()
Myclass.noObjects()

obj3 = Myclass()
Myclass.noObjects()
          
