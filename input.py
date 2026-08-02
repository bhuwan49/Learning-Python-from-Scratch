# input function to take input from user
name = input("Enter your name: ")
print("Hello, " + name + "!")
age = input("Enter your age: ")
if age.isdigit():
    print("You are", age, "years old.")
else:
    print("You are " + age + " years old.")
    