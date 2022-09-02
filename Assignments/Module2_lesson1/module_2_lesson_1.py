# # This function returns the maximum of three numbers
print("This function returns the maximum of any three numbers")
def maximum(x,y,z):
    return max(x,y,z)

x = float(input("Enter the first number here: "))
y = float(input("Enter the second number here: "))
z = float(input("Enter the third number here: "))

max_num = maximum(x,y,z)
print("The maximum number is " + str(max_num))


