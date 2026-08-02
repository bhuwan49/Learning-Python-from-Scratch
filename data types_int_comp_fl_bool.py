# Practical about data types in python
print("\n")
# numeric data types
print("Numeric Data Types:")
print("\n")
print("Integer values:")
a = 186        #decimal
b = 0b100110  #binary
c = 0o12      #octal
d = 0x1A      #hexadecimal

print("Decimal:", a) 
print("Binary:", b)
print("Octal:", c)
print("Hexadecimal:", d)

print("\n")
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))

print("\n")

print(isinstance(a, int))    # True
print(isinstance(b, float))  # False
print(isinstance(c, int))    # True
print(isinstance(d, int))    # True

# wow vs code is great

# float data types
x = 3.14
y = 2.5e3  # scientific notation
z = -0.001

print("\n")
print("Float values:")
print("x =", x)
print("y =", y)
print("z =", z)

print("\n")
print("Type of x:", type(x))
print("Type of y:", type(y))
print("Type of z:", type(z))

print("\n")
print(isinstance(x, float))  # True
print(isinstance(y, float))  # True
print(isinstance(z, float))  # True

print("\n")

# complex data types
p = 3 + 4j
q = 2 - 5j

print("Complex values:")
print("p =", p)
print("q =", q)

print("\n")
print("Type of p:", type(p))
print("Type of q:", type(q))

print("\n")
print(isinstance(p, complex))  # True
print(isinstance(q, complex))  # True
print("\n")

# boolean data types
r = True
s = False

print("Boolean values:")
print("r =", r)
print("s =", s)

print("\n")
print("Type of r:", type(r))
print("Type of s:", type(s))

print("\n")
print(isinstance(r, bool))  # True
print(isinstance(s, int))    #  **TRUE** despite being a boolean, 
#    because in Python, bool is a subclass of int 
#   (True is equivalent to 1 and False is equivalent to 0) 

print(isinstance(s, bool))  #True
print(isinstance(r, float))    #False 


print("\n")
print("All data types have been demonstrated successfully.")

# integer to float conversion
int_value = 10 
float_value = float(int_value)
print("Integer value:", int_value)
print("Converted to float:", float_value)
