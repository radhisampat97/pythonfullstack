####Changing of the case of string
####
####
##name = input('Enter your name: ')
##print(name)
##print('The id of name: ',id(name))
##print(name.upper())
##print('the id of name upper: ', id(name.upper()))
####
####b = name.upper()
#####
##print('This is upper case: ', name.upper())
##
##print('This is upper case: ', name.lower())
##
##print('This is swapcase: ', name.swapcase())
##
##print('This is tittlecase: ', name.title())
      
##
##
## concatination of string
##
##fname = 'Radhika'
##
##lname = 'Patel'
##
##education = 'B.SC-IT'
##
##location = 'Mumbai'
##
##mobile = 1234567890
##
##fullname = fname+' '+lname
##print(fullname)
##
####name to be printed on certification
##
##print('This is to certify Mr./Mrs' + ' ' + fname + ' ' + lname + ' ' + 'in' + ' ' + education + ' ' + 'branch' + '.')


##
## counting of string
### Understanding the counting of sub string we use count() method
##
###   main_string.count(substring)
##
###     main_string.count(substring, beinning, end)
##
##
##main_string = input('Enter main string: ')
##sub_string = input('Enter sub string: ')
##
##
##num = main_string.count(sub_string, 328, -290)
##print(num)
##
### count() method using starting and indexing numbers
##
##main_string = input('Enter main string: ')
##sub_string = input('Enter sub string: ')
####print(len(main_string))
##
##
##num = main_string.count(sub_string, 0, 74)


## formatting a string

fname = input('Enter your first name:')
mname = input('Enter your middle name:')
lname = input('Enter your last name:')

fullname = fname + ' ' + mname + ' ' + lname
#print(fullname)

print("My name is {}".format(fname))

print("This is my fullname {} {} {}".format(fname,mname,lname))

print(f'This is my fullname {fname} {mname} {lname}')
