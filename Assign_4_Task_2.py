# Task 2: Write and Append Data to a File

print("Enter text to write  to the file: ",end="")
string=input()
try:
    file1=open('output.txt','a')
    appending_file=file1.write(string+"\n")
    file1.close()
    print("Data successfully written to output.txt")
except:
    print("The file 'output.txt' is not found")
finally:
    print("Enter additional text to append:")
    string2=input()
    file1 = open('output.txt', 'a')
    appending_file = file1.write(string2)
    print("Data successfully appended")
    file1.close()

    file1 = open('output.txt','r')
    #file1 = open('My_file.txt','r+')    # read and write mode
    reading_file=file1.read()
    print("Final content of output.txt:\n",reading_file)
    file1.close()