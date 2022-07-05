# example for two exceptions
# a function to find total and average of list elements

def avg(list):
    tot = 0
    for x in list:
        tot += x
    avg = tot/len(list)
    return tot, avg

# call the avg() and pass a list
try:
    t,a = avg([1,2,3,4,5,6,7,8,9])
##   print(f'Total is {t} and average is {a}')

except TypeError:
    print('Type Error, please provide numbers.')
except ZeroDivisionError:
    print('ZeroDivision Error, please do not give empty list.')
finally:
    print(f'Total is {t} and average is {a}')
