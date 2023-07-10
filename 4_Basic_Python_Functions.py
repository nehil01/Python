
# Min function (Gives the minimum number persent in the bracket)
print(min(2,5,8,1,9,7))

# Max function (Gives the maximum number persent in the bracket)
print(max(1,5,9,2,4,8,11))


#Q. Write the python code to get three number as user inputs and
# print the maximum and minimum numbers on screen.


x = input("Enter 1st number ")
y = input("Enter 2nd number ")
z = input("Enter 3rd number ")

#minimum = min(x,y,z)
#maximum = max(x,y,z)

print("Minimum",min(x,y,z))
print("Maximum",max(x,y,z))


def avarage(no1, no2, no3):
 ans = (no1+no2+no3)/3
 return ans

print(avarage(10, 11, 12))
