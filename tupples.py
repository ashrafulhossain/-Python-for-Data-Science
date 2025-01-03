# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#access
tup = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tup[2:5])


tup = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tup[:4])

tup = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tup[-5:-2])

tup = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if 'apple' in tup:
    print('yes')
else:
    print('no')

#update tupples

countries = ('spain', 'bangladesh', 'usa', 'nepal', 'germany')
update_tup = list(countries)
update_tup.append('singapur')
countries = tuple(update_tup)
print(countries)



countries = ('spain', 'bangladesh', 'usa', 'nepal', 'germany')
update_tup = list(countries)
update_tup[3] = 'austria'
countries = tuple(update_tup)
print(countries)

countries = ('spain', 'bangladesh', 'usa', 'nepal', 'germany')
update_tup = list(countries)
update_tup.pop(1)
countries = tuple(update_tup)
print(countries)

name = ('ashra', 'shakib', 'nokib', 'jakir', 'karim')
name_one =('hossain',)
name += name_one
print(name)

name = ('ashra', 'shakib', 'nokib', 'jakir', 'karim')
name_rem = list(name)
name_rem.remove('karim')
name = tuple(name_rem)
print(name)


name = ('ashra', 'shakib', 'nokib', 'jakir', 'karim')
name_rem = list(name)
name_rem.pop(2)
name = tuple(name_rem)
print(name)


#unapacking tupple
name = ('ashra', 'shakib', 'karim')
(ashra, shakib, karim) = name
print(ashra)
print(shakib)
print(karim)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,  *red) = fruits
print(green)
print(yellow)
print(red)
print(type(yellow))
print(type(red))
print(type(fruits))

# joins tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

number = (2, 6, 8, 10)
number_tup = number * 2
print(number_tup)


