#from employee import da, hra, pf, itax
from employee import *

#using employee module to calculate gross and net
#salary of an employee

# calculate gross salary of employee by taking basic

basic = float(input('Enter basic salary: '))

# to calculate the gross salary

gross = basic + da(basic) + hra(basic)

print('Your gross salary: {}'.format(gross))

# calculate net salary
net = gross - pf(basic) - itax(gross)
print('Your net salary is: {}'.format(net))

