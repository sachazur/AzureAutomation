#import os for chdir and change directory
import os
os.chdir("C:/SachGit/Python/1stdsay")
#create a empty list
lis=[]
#import glob for searching *.py and #select all files with py extensions
import glob
lis = glob.glob("*.py")
#import zip for doing compression and #Create/open a zip file
import zipfile
z = zipfile.ZipFile("C:/SachGit/Python/pi.zip","w",zipfile.ZIP_DEFLATED)
for l in lis:
    print ("{} is getting added in zip".format(l))#display status
    z.write(l) #add zip file
z.close()
#close zip
