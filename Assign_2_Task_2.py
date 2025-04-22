print("Enter till which number you want to add from 1 to :", end="")
num=int(input())
i=1
sum=0
'''
while i<= num:
    sum=sum+i
    i=i+1
'''
for f in range(1,num+1):
    sum=sum+f
print("sum of numbers from 1 to ",num," is: ",sum)
