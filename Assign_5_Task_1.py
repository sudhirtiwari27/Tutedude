
#Task 1: Create a Dictionary of Student Marks


dict1={'Mike':95,'Alice':85, 'Allen':74}
print("Enter student's name: ")
name=input()
#print("All values in Dictionary :",dict1)
try:
    print(name,"'s marks:",dict1[name])
except:
    print("Student not found")



