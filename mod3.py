a, b = 'good','bad'
print (a,b)

joke = input("Put joke here: ")
print ('The killer', joke)

text = input("type python or not: ")
if "python" in text:
    print (text)
else:
    print ("Not python")
mylist = input("separates text into rows: ")
for x in mylist:
    print(x)

X = input("put 1st number: ")
Y = input("put 2nd number: ")
while X > Y:
        print ("X bigger")
else:
        print ("Y bigger")

def f(a,b,c=1,*d):
        print(a+b+c+d[0])

def f(a,b,c=1,*d):
        return a+b+c+d[0]
    
