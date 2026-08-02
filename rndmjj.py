text = "hello WORLD"
print(id(text))
# This leaves 'text' completely untouched!
# text.capitalize() 
print(text)  # Output: hello WORLD

# To keep the changes, save it to a new or existing variable
fixed_text = text.capitalize()
print(fixed_text)  # Output: Hello world

print(id(fixed_text))

g = "hello WORLD"

print(id(g))


# g[6] = "h"    ----->> ERROR
       


