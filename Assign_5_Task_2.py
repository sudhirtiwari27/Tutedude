
# Task 2: Demonstrate List Slicing

x=[]
for i in range(1,11):
    x.append(i)
print("Original list: ",x)
ext=x[0:5]
print("Extracted first five elements: ",ext)
rev=list(reversed(ext))
print("reversed extracted: ",rev)

