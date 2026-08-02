s = "Bhuwan"
for index,character in enumerate(s):
    print(index,"--->",character)
print(list(enumerate(s)))
print(enumerate(s))

print(s)
print(*s)
print("------------------------------")

print(s, sep=" ")
print(*s, sep="$")

print("-------------------")

print(*s, sep = "\n")

s = "Bhuwan"
for index, character in enumerate(s):
    print(index,end=" ,")
    

print(sorted("bhuwan",reverse=True))

print(sorted("bhuwan"))


