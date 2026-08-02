print("\n\n")

#Sets are unordered collections of unique items.
set_1 = {1, 2, 3, 4, 5}
set_2 = {'apple', 'banana', 'cherry'}
set_3 = {1, 'hello', 3.14}

print("set_1 = ", set_1)
print("set_2 = ", set_2)
print("set_3 = ", set_3)

print("\n\n")
#type() function can be used to check the type of a variable.
print("class of set_1: ", type(set_1))
print("class of set_2: ", type(set_2))
print("class of set_3: ", type(set_3))

print("\n\n")
#isinstance() function can be used to check 
# if a variable is an instance of a specific type.
print("is set_1 an instance of set? ", isinstance(set_1, set))
print("is set_2 an instance of set? ", isinstance(set_2, set))
print("is set_3 an instance of set? ", isinstance(set_3, set))
print("is set_1 an instance of int? ", isinstance(set_1, int)) # This will return False since set_1 is not an integer.

print("\n\n")
