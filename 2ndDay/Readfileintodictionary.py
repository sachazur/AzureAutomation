''''f=open("input2.txt",'r')                    #open file
d={}                                        #create a dict
for line in f:                              #read line by line   
    key,value=line.strip().split('=')       #split line
    d[key]=value                            #add key value
f.close()                                   #close file
print (d)'''
#multiline comments with """ or '''

f=open("input2.txt",'r')                    #open file
d={}                                        #create a dict
for line in f:                              #read line by line   
    line=line.strip()
    if line and not line.startswith('#'):
        key,value=line.strip().split('=')       #split line
        d[key]=value                            #add key value
f.close()                                   #close file
print (d)


