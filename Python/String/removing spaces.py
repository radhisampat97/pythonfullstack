##understanding the removing of black/white spaces from string

##right strip to remove the blank spaces from right
#rstrip()

##left strip to remove the blank spaces from left
#lstrip()

##strip to remove the blank spaces from both sides
#strip()


name1 = 'anurag     '
name2 = '      anurag'
name3 = '     anurag        '

print(name1)
print(name2)
print(name3)

##print(name1.rstrip())
##print(name2.lstrip())
##print(name3.strip())

if 'anurag' == ' anurag  ':
    print('yes')
else:
    print('no')


