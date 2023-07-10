
iteration = 1
total = 0

while iteration<=10:
    number = int(input("Enter Number "))
    total = total + number
    iteration = iteration + 1 
print("sum is",total)


# To calculate factorial
fact = int(input("Enter no. to calculate factorial "))
result = 1
while fact>=1:
    result = result * fact
    fact = fact-1
print("factorial is", result)