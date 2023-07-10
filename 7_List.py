thislist = ["apple", "banana", "mango"]
print(thislist)
print(len(thislist))

# to access an item
print(thislist[1])

# ranges of Indexes

list = ["apple", "banana", "mango", "cherry", "pineapple", "berry"]
print(list[2:5])
print(list[:4])

# To check an item on the list
if "apple" in list:
    print("Yes apple is present in the list")

# Change the item
list[1]= "blueberry"
print(list)

# Insert item
list.insert(2, "watermelon")
print(list)

# Append list (insert item at last of the list)
list.append("orange")
print(list)

# extend a list
list.extend(thislist)
print(list)

# to Remove an item 
list.remove("orange")
print(list)
# OR
del list[2]
print(list)

# to Clear the list
list.clear()
print(list)

# Loop Through a list
thelist = ["apple", "banana", "mango", "cherry", "pineapple", "berry"]
for x in thelist:
    print(x)

# List Comprehension (Creates a new list By changing an Existing element)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
        print(newlist)

""" 
    SORT
    LIST
"""

# sort Alphabatically
thelist.sort()
print(thelist)

# to sort in Reverse order
thelist.sort(reverse=True)
print(thelist)

# To copy the list

mylist = thelist.copy()
print(mylist)

# Join two lists
list1 = [1, 2, 3, 4]
list2 = ["A", "B", "C", "D"]

#1st method
list3 = list1 + list2
print(list3)

#2nd method
list1.extend(list2)
print(list1)

# EXAMPLE



x = ["apple","banana","cherry","berry",13,24,76]

i = 0

while i<len(x):
 print(x[i])
 i = i+1

# SLICING

print(x[2:])
print(x[:4])
print(x[0:5:2])