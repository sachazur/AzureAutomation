#read file contents at once
f=open('input.txt','r')
print(f.read())
f.close()

#read file char by  char
f=open('input.txt','r')
print(f.read(1))
print(f.read(1))
f.close()

#read file line by line
f=open('input.txt','r')
print (f.readline())
print (f.readline())
f.close()


#read all lines into a list
f=open('input.txt','r')
lines = f.readlines()
print(lines[2])
print(lines)
f.close

#append to existing file
f=open('input.txt','a')
f.write("\nthis is a new line")
f.close

#Write into a new file
f=open("input3.txt",'w')
f.write("this is line one")
f.close()

f=open("C:\input.txt","r")
for line in f:
    #print (line,end="")
    print (line.strip())#remove white space other options line.rstrip and line.lstrip
f.close()

f=open("C:/sachin/Pythontrain1/2ndDay/input2.txt","r")
for line in f:#read line by libe
    x=line.index("=")
    #print (line,end="")
    print(line[0:x])#remove white space other options line.rstrip and line.lstrip
f.close()



