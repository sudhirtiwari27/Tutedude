
#Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))

print("Enter a number: ", end="")
num=int(input())
ans=factorial(num)
print("Factorial of ",num," is: ",ans)
