def vowelcount(s):
    count = 0
    print (type(s))
    vowels="aeiou"
    for x in s.lower():
        if x in vowels:
            count = count + 1 
    return count

def get_indices(word,char):
    lis=[]
    for l in range(len(word)):
        if word[l] == char:
            lis.append(l)
    return lis

def get_indices1(word,char):
    lis=[]
    for index,mychar in enumerate(word):
        if mychar == char:
            lis.append(index)
    return lis
      
    
        
        
            
    
