###list methods

num = [5106, 5106516, 60545, 651896, 65160, 'start', 682, 3242668125, 816, 66810, 681, 352, 601, 324258761, 1351, 651, 'start']

##list.index()
##to find the first occurrence of start
first_occur = num.index('start')
print('First occurrence: ', first_occur)

##list.append()
##to add a new element at the end of the list
new = [0,1,2,3,4]
print(new)
new.append(5)
print(new)

##list.insert(i, x) i = index, x = value
# to a a particular value to a particular index
new = [0,1,2,3,4]
print(new)
new.insert(2, 'start')
print('After insertion: ', new)
##
# list.copy()
##to copy all the lsit elements into a new list and return it
latest = new.copy()
print('The latest list: ', latest)
###
## list .extend()
#to extend the existing list with another list

a = [0,1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)
print('extended list: ', a)

###
## list.count(value)
## to count the number of occurrance

a = [0,1,2,3,4,4,4,4,4,5,6,7,7,7,8,8,8,8,8,9,9,9,9,1,1,1,1,1,1,1,1,15]
print(a.count(1))

##
## list.pop()
##to remove the elements from the last we use pop()

a = [632484, 63245165, 36184368, 41,631,4,5530]
##print(a)
##print(a.pop())
##print(a)
###
##list.sort()
## to sort the elements of the list in asscending order
print(a)
a.sort()
print(a)
###
## list.reverse()
# it will reverse the list
a.reverse()
print(a)

###
### list.clear()
# deletes all elements from the list
a.clear()
print(a)
      
