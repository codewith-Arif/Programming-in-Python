# n = int(input("enter number : "))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print('factorial =',fact)  

n = int(input("enter number : "))

i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print("factorial = ",fact)    