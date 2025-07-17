try:
    file1 = open('sample.txt','r')
    print("reading file contain")
    file_reading=file1.read()
    print(file_reading)
    file1.close()

except FileNotFoundError :
    print("the file text sample.txt was not found")