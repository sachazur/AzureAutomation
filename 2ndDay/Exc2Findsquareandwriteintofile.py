#You can only write string to a file
f=open("squares.txt","w")       #open file
for i in range(100):            #range of 100
    value = i*i                 #square
    f.write(str(value) + "\n")         #writelines
f.close()   

    #or

with open("squares2.txt","w") as fout:
    for x in range(100):
        fout.write(str(x*x)+ "\n" )
