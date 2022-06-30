# dictionary methods

detail = {'Name':'Anurag',
          'Location':'Thane',
          'Mobile': 9892631384,
          'Coding':'Python'
          }

#dict.values() to get all the values from the dictionary

a = list(detail.values())
print(a)
print(type(detail.values()))
print()

## dict.keys() to get all the keys from dictionary

b = list(detail.keys())
print(b)
print(type(detail.keys()))
print()

## dict.update() to add a new key-value pair to the dictionary
detail.update({'Surname':'Chiplunkar'})
print(detail)
print()

## dict.setdefault() returns a value of the specified key, if the key is not present
## insert the key with the specified value

detail.setdefault('Company', 'Freelancer')
print(detail)
print()

## dict.popitem() removes the last inserted key-value pair

detail.popitem()
print(detail)
print()

##dict.pop() removes the element with the specified key
#details.pop('Surname')

detail.pop('Mobile')
print(detail)
print()

## detail.items() returns a list containing a tuple for each key value pair

a = detail.items()
print(a)
print()

## dict.fromkeys()(sequence, default_value) returns a dictionary with the
##specified keys and values

tup = ('Name', 'Surname', 'Age', 'Company', 'Location')
values = 'Default'
detail = detail.fromkeys(tup, values)
print(detail)
print()

## dict.copy() returns a copy of the ddictionary

duplicate = detail.copy()
print('Identity of detail: ', id(detail))
print(detail)

print()
print('Identity of duplicate: ', id(duplicate))
print(duplicate)
print()

## dict.get(key, message) returns the value for the given key

a = detail.get('Name', 'No such key present')
print(a)
print()

## to find the length of dictionary

print('The length of the dictionary is: ', len(detail))
print(detail)
print()

## dict.clear() this will remove all the elements from the dictionary

detail.clear()
print(detail)

