## creating a class for patient appointment
##with methods of booking appointment
## calling appointment

class Patient:
    ''' '''
    def __init__(self, n = ' ', age =0, m=0, d='', c=''):
         self.name = n
         self.age = age
         self.mobile = m
         self.doctor = d
         self.conditions = c

    def booking(self):
         print('Preferred time: ' , time)
         print("This is to inform you that you appointment is fixed for "+time+"pm")
         print()

    def calling(self):
            print('Hi, Patient name: ', self.name)
            print('Your age: ', self.age)
            print('This is mobile number: ', self.mobile)
            print('This is my doctor: ', self.doctor)
            print('My previous medical condition: ',self.conditions)


name = input('Enter Patient name: ')
age = input('Enter Patient age: ')
mobile = input('Enter Patient mobile number: ')
doctor = input('Enter Doctors name: ')
conditions = input('Enter Patient conditions: ')
time = input('Enter preferred time:')


# constructor called without any arguments

a = Patient(name,age,mobile,doctor, conditions)
##a = Patient('Radhika',25,123456789 ,'Dilip','Skin')
a.booking()
a.calling()
print('----------')



