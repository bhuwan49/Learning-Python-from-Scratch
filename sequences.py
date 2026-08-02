print("\n\n")

#Lets talk about sequences in python. 
# A sequence is an ordered collection of items. 
# Python has several built-in sequence types, including lists, tuples, and strings. 
# Each of these types has its own characteristics and uses.




print("\n\n")

# Strings are sequences of characters. 
# They are immutable, meaning that once a string is created, it cannot be changed. 
# You can create strings using single quotes, double quotes, 
# or triple quotes for multi-line strings.

string_1 = 'Hello, World!'
string_2 = "Python is awesome!"
string_3 = '''This is a multi-line string.
It can span multiple lines.'''

print("string_1 = ", string_1)
print("string_2 = ", string_2)
print("string_3 = ", string_3)

print("\n\n")
#type() function can be used to check the type of a variable.
print("class of string_1: ", type(string_1))
print("class of string_2: ", type(string_2))
print("class of string_3: ", type(string_3))

print("\n\n")
#isinstance() function can be used to check 
# if a variable is an instance of a specific type.
print("is string_1 an instance of str? ", isinstance(string_1, str))
print("is string_2 an instance of str? ", isinstance(string_2, str))
print("is string_3 an instance of str? ", isinstance(string_3, str))
print("is string_1 an instance of int? ", isinstance(string_1, int)) # This will return False since string_1 is not an integer.

print("\n\n")
# Lists are ordered collections of items.
list_1 = [1, 2, 3, 4, 5]
list_2 = ['apple', 'banana', 'cherry']
list_3 = [1, 'hello', 3.14]

print("list_1 = ", list_1)
print("list_2 = ", list_2)
print("list_3 = ", list_3)

print("\n\n")
#type() function can be used to check the type of a variable.
print("class of list_1: ", type(list_1))
print("class of list_2: ", type(list_2))
print("class of list_3: ", type(list_3))

print("\n\n")
#isinstance() function can be used to check 
# if a variable is an instance of a specific type.
print("is list_1 an instance of list? ", isinstance(list_1, list))
print("is list_2 an instance of list? ", isinstance(list_2, list))
print("is list_3 an instance of list? ", isinstance(list_3, list))
print("is list_1 an instance of int? ", isinstance(list_1, int)) # This will return False since list_1 is not an integer.

print("\n\n")

#Tuples are ordered collections of items, similar to lists.
# However, tuples are immutable, meaning that once a tuple is created, it cannot be changed
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = ('apple', 'banana', 'cherry')
tuple_3 = (1, 'hello', 3.14)
tuple_4 = 1,2,3,4,5 # This is also a tuple, even without parentheses.
tuple_5 = ('apple',) # This is a tuple with a single element. The comma is necessary to indicate that it is a tuple.
tuple_6 = apple, banana, cherry = 'apple', 'banana', 'cherry' # This is tuple unpacking. The values on the right are assigned to the variables on the left.

print("tuple_1 = ", tuple_1)
print("tuple_2 = ", tuple_2)
print("tuple_3 = ", tuple_3)
print("tuple_4 = ", tuple_4)
print("tuple_5 = ", tuple_5)
print("tuple_6 = ", tuple_6)

print("\n\n")
#type() function can be used to check the type of a variable.
print("class of tuple_1: ", type(tuple_1))
print("class of tuple_2: ", type(tuple_2))
print("class of tuple_3: ", type(tuple_3))
print("class of tuple_4: ", type(tuple_4)) 
print("class of tuple_5: ", type(tuple_5))
print("class of tuple_6: ", type(tuple_6))

print("\n\n")
#isinstance() function can be used to check
# if a variable is an instance of a specific type.
print("is tuple_1 an instance of tuple? ", isinstance(tuple_1, tuple))
print("is tuple_2 an instance of tuple? ", isinstance(tuple_2, tuple))
print("is tuple_3 an instance of tuple? ", isinstance(tuple_3, tuple))
print("is tuple_4 an instance of tuple? ", isinstance(tuple_4, tuple))
print("is tuple_5 an instance of tuple? ", isinstance(tuple_5, tuple))
print("is tuple_6 an instance of tuple? ", isinstance(tuple_6, int)) # This will return False since tuple_6 is not a tuple, it is an integer.
