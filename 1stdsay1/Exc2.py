mylist=[]
while True:
    num=input("Number Please:")
    if num.lower() != "end":
        mylist.append(int(num))
    else:
        break
print(sum(mylist))
