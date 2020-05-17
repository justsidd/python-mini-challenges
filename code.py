# --------------
#Code starts here

def palindrome(num):
    x=num+1
    y=str(x)
    while y[0:]!=y[len(y)::-1]:
        x+=1
        y=str(x)
    return x
palindrome(8)
    




# --------------
#Code starts here
def a_scramble(str_1,str_2):
    s1=str_1.lower()
    s2=str_2.lower()
    for x in range(len(s2)):
        if s1.count(s2[x])==s2.count(s2[x]):
            a=True
        else:
            a=False
    return a
a_scramble("baby shower","shows")


# --------------
#Code starts here
def check_fib(num):
    lst=[0,1]
    for x in range(20):
        lst.append(lst[x]+lst[x+1])
    if num in lst:
        return True
    return False



# --------------
#Code starts here
def compress(word):
    words=word.lower()
    count=1
    length=""
    if len(words)>1:
        for i in range(1,len(words)):
            if words[i-1]==words[i]:
                count+=1
            else :
                length += words[i-1]+str(count)
                count=1
        length += (words[i]+str(count))
    else:
        i=0
        length += (words[i]++str(count))
    return (length)        



# --------------
#Code starts here
def k_distinct(string,k):
    lst=[]
    for x in string.lower():
        if x not in lst:
            lst.append(x)
    if len(lst)==k:
        return True
    return False 
    
k_distinct('Messoptamia',8)


