def fact(a):
    prod=1
    for i in range(1,a+1):
        prod=prod*i
    return prod
 
a=int(input("Enter number"))
b=fact(a)
print("Factorial of ",b," is:",b)
