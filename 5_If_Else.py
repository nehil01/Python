
a = 10
b = 30
if(a<b):
    print("B is greater")
else:
    print("A is greater")

x = 33
y = 33
if(x>y):
    print("X is greater")
elif x==y :
    print("x is equal to y")

# Or (short method)
print("A is smaller") if a<b else print("B is smaller")



#Age


Age = int(input("Enteryour age "))
if Age >= 18 :
    print("Drive")
else:
    print("Cannot Drive")




#Nested If


age = int(input("Enter your age "))
#icheck whether age is greater than 18
if age > 18 :
    #check if age is greater than 65
    if age >= 65:
        print("Take rest")
    #if age is smaller than 65
    else:
        print("You are eligible to drive")
#if age is smaller than 18
else:
    print("Wait till you are 18")

    

# To check a figure is rectangle or a square

length = int(input("Enter the length "))
breadth = int(input("Enter the breadth "))

if length == breadth:
    print("Figure is square")
else:
    print("Figure is rectangle")