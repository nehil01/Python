# Multiple line string
a = """hello....
.........
........
........
........
........"""
print(a)

#strings are arrays
x = "hello"
print(x[1])

#loops in string 'for loop'
for x in "hello":
  print(x)

# String length
a = "hello world"
print(len(a))

# Replacing String

x = "Hello"
print(x.replace("H","J"))

# Split String
a = "Hello, World"
print(a.split(","))

# String Concatenation
a = "hello"
b = "world"
print(a+b)
# or
c = a +" " + b
print(c)

# String Format
age = 20
txt = "My Name is Nehil, I am {}"
print(txt.format(age))

quantity = 3
itemno = 128
price = 200
txt = "I want {} items of section {} of worth Rs. {}"
print(txt.format(quantity,itemno,price))
