# Precedence and associativity of operators in Python
# write an example code to demonstrate the precedence and associativity of operators in Python.
# Example code to demonstrate the precedence and associativity of operators in Python
print(2 + 3 * 4)  # Output: 14 (multiplication has higher precedence)
print((2 + 3) * 4)  # Output: 20 (parentheses override precedence)
print(2 ** 3 ** 2)  # Output: 512 (exponentiation is right-associative)
print(2 ** (3 ** 2))  # Output: 512 (parentheses override associativity)
print(10 - 3 + 2)  # Output: 9 (subtraction and addition are left-associative)
#logical operators
print(True and False or True)  # Output: True (and has higher precedence than or)
print((True and False) or True)  # Output: True (parentheses override precedence)
print(not True and False)  # Output: False (not has higher precedence than and)
a,b,c,d,e,f = 1,1,2,2,3,3
print(a==b or c==d and e==f)  # Output depends on the values of a, b, c, d, e, f 
                            # (and has higher precedence than or)
print((a==b or c==d) and e==f)  # Output depends on the values of a, b, c, d, e, f
print((a==b or c==d) and (e==f))  # Output depends on the values of a, b, c, d, e, f