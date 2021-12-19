def intersect(seq1,seq2):
    res = [] #blank list
    for item in seq1:
        if item in seq2:
            res.append(item)
    return res

s1 = "SPAM"
s2 = "SCAM"

print (intersect (s1,s2))

x1 = [1,2,3,4]
x2 = [3,4,5,7]
print (intersect(x1,x2))

x = 99
def func():
    x = 88 #is local to the scope
    y = 9
    print (x)

print (x) #will print main function
print (y) #wont print since y is exclusive to function

