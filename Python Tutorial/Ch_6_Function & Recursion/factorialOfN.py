#WAF to find the factorial of n.(n is the parameter)


# def find_fact(n):
#     fact =1
#     i = 1
#     while i <= n:
#         fact *= i
#         i += 1
#     print(fact)    

# find_fact(5)

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact(2)
