#the order of tuples are unchangable

thistuple = ("apple", "banana", "cherry")
print(thistuple) 

# Tuple length
print(len(thistuple))

# Another way to create tuple
thistuple = tuple(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
print(thistuple)

# Accessing Touple items
print(thistuple[1])

# Range of Indexes
print(thistuple[2:4])

# check if item exist in tuple
if "cherry" in thistuple:
    print("Yes, cherry exist in thistuple")

#convert values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "lemon"
x = tuple(y)
print(x)
