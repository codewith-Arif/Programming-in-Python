a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))

if(a>b and a>c):
    greatest = a
elif(b>a and b>c):
    greatest = b
else:
    greatest = c

print("greatest number is",greatest)


