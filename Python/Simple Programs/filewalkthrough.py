file1 = open('file1.txt')

read_content1 = file1.read()

print(read_content1)

#oepn the file.txt in write mode

file2 = open('file2.txt', 'w')

#write content
file2.write('Programming is Fun. \n')
file2.write("Hinga Dinga Durgen \n")

file2.close()

file2= open('file2.txt', 'r')
read_content2 = file2.read()

print(read_content2)

#good practice -- close all files

file1.close()
file2.close()

#most efficient -- use this method

with open("file1.txt", "r") as mess:
    read_content = mess.read()
    print(read_content)