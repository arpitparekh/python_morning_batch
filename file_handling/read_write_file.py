# file read and write

f = open('/home/arpit-parekh/files/hello.txt','w')
f.write("This my file")
f.write("writting in a file using python")
f.writelines("This is new line in file")
f.writelines("This is python")
f.close()

f1 = open('/home/arpit-parekh/files/hello.txt','r')
print(f1.readline())
f1.close()   # remove object from memory