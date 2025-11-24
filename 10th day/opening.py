#basic file opeing code
file = open("example.txt","r")
#read whole content at once
content = file.read()
print(content)


print('--------------------------------------------------------')
#read only first line
file = open("example.txt","r")
line = file.readline()
line2 = file.readline()
print(line)
print(line2)


print('---------------------------------')
#line printing according to user choice
with open("example.txt","r") as f:
    lines = f.readlines()

print(lines[0])

file.close()


