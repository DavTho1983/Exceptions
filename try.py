try :
    f = open('hello.txt', 'r') #only has read permission - 'w' has write permission
    f.write("Test write to simple text!")
except IOError : #no need to specify particular error
    print('Error: could not find file or read data!')
else :
    print("SUCCESS!")
    f.close()
finally :
    print("hello world!")
