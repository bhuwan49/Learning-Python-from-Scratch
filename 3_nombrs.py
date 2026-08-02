a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b == c:
    print("All three numbers are equal")
    
else:
    greatest = max(a, b, c)
    smallest = min(a, b, c)
    print("Greatest number is", greatest)
    print("Smallest number is", smallest)
