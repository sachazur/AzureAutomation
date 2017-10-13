from os import system
with open("C:/sachin/Pythontrain1/2ndDay/IP.txt","r") as f:
    lis = f.readlines()
    for i in lis:
        i = i.strip()
        pingstring = "ping -n 1 {} > nul".format(i)
        status = system(pingstring)
        if status:
            print ("{} is down".format(i))
        else:
            print ("{} is up".format(i))
        
    
