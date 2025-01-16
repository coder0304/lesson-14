def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x==0 or x==1:
     return 1
    else:
       return x*factorial(x-1)
    
print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 1:",factorial(1))
print("the factorial of 89:",factorial(89))
print("the factorial of 8:",factorial(8))
print("the factorial of 6:",factorial(6))