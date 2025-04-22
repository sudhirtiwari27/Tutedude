
print("Enter a number: ",end="")

num=int(input())
print(num," is an ",end="")
r=num%2
if (r > 0):
    print("Odd number")
else:
    print("Even number")
