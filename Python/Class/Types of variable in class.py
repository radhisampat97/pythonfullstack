# Types of variables in classes

# 1 Instance variable
# 2 Class Variables or static variable
##
#instance var example

class Sample:
     '''This is a simple instance variable'''
     # this is a constructor
     def __init__(self):
          self.x = 10 # this is an instance variable

     # this is an instance method
     def modify(self):
          self.x +=1


a = Sample()
##xyz = Sample()
print(a.x)
a.modify()
print(a.x)
xyz = Sample()
print(xyz.x)


### create 2 instance

s1 = Sample()
s2 = Sample()

s1.modify()
s1.modify()
s1.modify()
print('x in s1: ', s1.x)
print('x in s2: ', s2.x)
print()

### Class Variables or Static Variables example

# class vars or static variables example

class Sample:
    #this is a class var or static variable
    x = 10

    #this is a class method
    @classmethod
    def modify(cls):
        cls.x += 1

# create 2 instances
s1 = Sample()
s2 = Sample()

print('x is s1 = ', s1.x)
print('x is s2 = ', s2.x)

##
### modify x in s1 only
s1.modify()
s1.modify()
s1.modify()
print('x is s1 = ', s1.x)
print('x is s2 = ', s2.x)



