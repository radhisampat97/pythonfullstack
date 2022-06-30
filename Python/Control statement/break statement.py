#using break to come out of a while loop
 
x = 10

while x >= 1:
     x -= 1
     if x ==5:
         break
     print('x: ', x)

print('Out of the loop')

##pass
x = 10

while x >= 1:
     x -= 1
     if x ==5:
         pass
     print('x: ', x)

print('Out of the loop')

##continue
x = 10

while x >= 1:
     x -= 1
     if x ==5:
         continue
     print('x: ', x)

print('Out of the loop')

