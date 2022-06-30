#Examples for Arithmetic Operators

#lets assign some values to variable
a=13
b=5
##a,b = 13,5

#Addition operator
c= a+b
print("Addition of 'a' and 'b' is: ", c)
print("This is the identity of c: ", id(c))
print("Addition of 'a' and 'b' is: ", a+b)
print("This is the identity of a+b: ", id(a+b))
##
##
##Subtraction operator
c= a-b
print("Subtracting of 'a' and 'b' is: ", c)
print(id(c))
print("Subtracting 'b' from 'a' gives: ", a-b)
print(id(a-b))

##
##Multiplication operator
c= a*b
print(id(c))
print(id(a*b))
print("Multiplication of 'a' and 'b' is: ", a*b)

##Division Operator
print('The value of a: ', a)
print('The value of b: ', b)
print()

##Modulus operator
print('The value of a: ', a)
print('The value of b: ', b)
print("Modulus of 'a' by 'b' gives remainder: ", b % a)

##Exponent operator
print('The value of a: ', a)
print('The value of b: ', b)
print("Exponent of 'a' to the power 'b' is: ", a**b)

##Integer Division operation
print('The value of a: ', a)
print('The value of b: ', b)
print("Integer Division of 'a' by 'b' gives integer value of quotient: ", a//b)
##
##
##Order of evaluation

x=1; y=2; z=3; a= 2; b=2; c=3
result = (x + y)*z**a//b+c
print("The answer for oder of evaluation is: ", result)

##Order of evaluation

x=3; y=1; z=3
result = x*y**z
print("The answer for oder of evaluation is: ", result)








