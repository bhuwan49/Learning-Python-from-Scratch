print("\n\n")


#Dictionaries are unordered collections of key-value pairs.

dict_1 = {'name': 'John', 'age': 30, 'city': 'New York'}
dict_2 = {1: 'apple', 2: 'banana', 3: 'cherry'}
dict_3 = {'name': 'John', 1: [2, 4, 3], 'age': 30}
dict_4 = dict(name='John', age=30, city='New York') # This is another way to create a dictionary.   

print("\n\n")
print("dict_1 = ", dict_1)
print("dict_2 = ", dict_2)
print("dict_3 = ", dict_3)
print("dict_4 = ", dict_4)

print("\n\n")
#type() function can be used to check the type of a variable.
print("class of dict_1: ", type(dict_1))
print("class of dict_2: ", type(dict_2))
print("class of dict_3: ", type(dict_3))
print("class of dict_4: ", type(dict_4))

print("\n\n")
#isinstance() function can be used to check
# if a variable is an instance of a specific type.
print("is dict_1 an instance of dict? ", isinstance(dict_1, dict))
print("is dict_2 an instance of dict? ", isinstance(dict_2, dict))
print("is dict_3 an instance of dict? ", isinstance(dict_3, dict))
print("is dict_4 an instance of int? ", isinstance(dict_4, int))

print("\n\n")
