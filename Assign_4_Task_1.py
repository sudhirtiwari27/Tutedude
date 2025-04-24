
#Task 1: Read a File and Handle Errors
try:
    file1 = open('my_file.txt','r')
    reading_file=file1.read()
    print(reading_file)
    file1.close()
except:
    print("The file 'sample.txt' is not found")


