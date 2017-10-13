import os

for (dirname,subdir,files) in os.walk('c:\\'):
    for myfile in files:
        filename=os.path.join(dirname,myfile)
        if  myfile.endswith(".txt") and os.path.getsize(filename) > 1024*1024:
            print(filename)     


#get txt file with size more than 1 MB size
