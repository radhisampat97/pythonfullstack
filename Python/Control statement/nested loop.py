##display the start pattern in right angled triangle

#range(start, stop-1, step)

for i in range(1, 11):
    for j in range(1, i+1):
       print('*',end='')
    print()

##display numbers from 1 to 100 in 10 rows and 10 cols
for x in range(1, 11):
##     print('The value of x: ',x)
     for y in range(1, 11):
##     print('The value of y: ',y)
        print('{}'.format(x*y), end='\t')


print('Python', end=',')
print('Java', end=',')
print('C++', end='.')
print('Javascript')
print('HTML')
