# This program finds the exponentiation of a number

print("This program finds the exponentiation of a number !!") 

def exponent(x,y):
          return 1 if y == 0 else x ** y

x = int(input("Enter the base value here: "))
y = int(input("Enter the exponential value here: "))

x= exponent(x,y)
print("Your answer is "+ str(x))